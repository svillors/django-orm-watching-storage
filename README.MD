# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка "Каждый день". Если вы попали в этот репозиторий случайно, то он не будет работать, но вы можете его использовать для вёрстки.

Пульт используется для просмотра визитов в хранилище и карточек сотрудников банка.

## Как установить
В коде присутсвуют переменные среды нужные для правильной его работы: DATABASE_HOST - адрес базы данных, DATABASE_PORT - порт, DATABASE_NAME - имя базы данных, DATABASE_USER - имя пользователя, DATABASE_PASSWORD - пароль для достпуа в базу данных, DJANGO_SECRET_KEY - секретный ключ проекта, DEBUG - настройка для дебага

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.