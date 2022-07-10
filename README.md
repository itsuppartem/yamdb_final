# YaMDb API (final)
## Описание

API для проекта, посвященного сбору ревью на различные произведения. 

Позволяет просматривать, создавать, редактировать, удалять и исправлять отзывы, комментарии, произведения, категории, жанры и т.п.

## WORKFLOW

При событии push в репозиторий гитхаб, происходит автоматическая првоерка "пуша" тестами в workflow(pep8, docker image biuld and push to docker hub, deploy на сервер ЯндексОблака, отписка в телеграм об успешной отработке workflow).

Переменные окружения хранятся на GitHub в разеделе Secrets
   * SECRET_KEY
   * DB_ENGINE
   * DB_NAME
   * POSTGRES_USER
   * POSTGRES_PASSWORD
   * DB_HOST
   * DB_PORT
Касаются Django проекта
   * TELEGRAM_TO
   * TELEGRAM_TOKEN
Касаются посылки в телеграмм
   * DOCKER_PASSWORD 
   * DOCKER_USERNAME
Касаются пуша на DockerHub
   * USER
   * HOST
   * SSH_KEY
   * PASSPHRASE
Касаются деплоя на сервер ЯндексОблако

## Локальный запуск проекта:

### Клонировать репозиторий:

```python
git clone https://github.com/itsuppartem/yamdb_final
```

### Перейти в директорию infra/ и запустить docker-compose:

```python
cd infra/
docker-compose up
```

### Применить миграции:

```python
docker-compose exec web python manage.py migrate
```

### Создать суперпользователя:

```python
docker-compose exec web python manage.py createsuperuser
```

### Cобрать статические файлы::

```python
docker-compose exec web python manage.py collectstatic --no-input
```

## Заполнение базы данными:

```python
docker-compose exec web python manage.py loaddata fixtures.json
```


## Проект развернут на Яндекс.Облако

http://51.250.98.36/redoc/  Документация по API

## Автор workflow:
Гуляев Артем

## Авторы YaMDb 
### Гуляев Артем
### Чуняев Павел
### Кальсин Дмитрий


## Бейдж


[![Django-app workflow](https://github.com/itsuppartem/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/itsuppartem/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)