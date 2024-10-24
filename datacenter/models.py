from django.db import models
import django.utils.timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if not self.leaved_at:
            seconds = (django.utils.timezone.now()
                       - self.entered_at).total_seconds()
            return seconds
        seconds = (self.leaved_at - self.entered_at).total_seconds()
        return seconds

    def format_duration(self):
        seconds_in_hour = 3600
        seconds_in_minute = 60
        hours, remainder = divmod(self.get_duration(), seconds_in_hour)
        minutes, seconds = divmod(remainder,  seconds_in_minute)
        return str(f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}')

    def is_visit_long(self, minutes=60):
        seconds_in_minute = 60
        return self.get_duration()/seconds_in_minute > minutes
