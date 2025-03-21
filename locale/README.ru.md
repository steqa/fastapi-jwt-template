[en](../README.md) [ru](README.ru.md)

# Fast JWTemplate :rocket:

![GitHub Release](https://img.shields.io/github/v/release/steqa/fast-jwtemplate) ![License](https://img.shields.io/badge/license-MIT-green)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-D02C2A?style=flat&logo=redis&logoColor=white) ![Alembic](https://img.shields.io/badge/Alembic-b57414?style=flat&logo=python&logoColor=white)

## Содержание
1. [Описание](#описание)
2. [Функциональность](#функциональность)
3. [Требования](#требования)
4. [Установка](#установка)
5. [Использование](#использование)
6. [Лицензия](#лицензия)
## Описание

Это шаблон для FastAPI-приложения с JWT аутентификацией. Он использует PostgreSQL для базы данных и Redis для черного списка refresh-токенов. Проект контейнеризирован с помощью Docker.

## Функциональность

- Безопасная JWT аутентификация пользователей с хэшированием паролей через bcrypt
- API-эндпоинты для входа, выхода и обновления токенов с обработкой истечения срока действия
- Черный список обновляемых токенов в Redis для повышения безопасности
- Создание пользователя с проверкой пароля

## Эндпоинты

1. **Вход пользователя**
	- _**POST**_ `/api/v1/auth/jwt/login`
	- _**Описание**_: Аутентифицирует пользователя и возвращает access и refresh токены.
2. **Обновление токена**
	- _**POST**_ `/api/v1/auth/jwt/refresh`
	- _**Описание**_: Обновляет access токен с использованием предоставленного refresh токена.
3. **Выход пользователя**
	- _**POST**_ `/api/v1/auth/jwt/logout`
	- _**Описание**_: Выходит из системы, блокируя refresh токен.
4. **Создание пользователя**
	- _**POST**_ `/api/v1/users`
	- _**Описание**_: Создаёт нового пользователя в системе.
5. **Получение информации о текущем пользователе**
	- _**GET**_ `/api/v1/users/me`
	- _**Описание**_: Возвращает данные текущего аутентифицированного пользователя.

## Требования

Убедитесь, что Docker установлен и запущен на вашей системе. Скачать Docker можно [здесь](https://www.docker.com/get-started).

## Установка

1. **Клонируйте репозиторий**

	```bash
	git clone https://github.com/steqa/fast-jwtemplate.git project-folder
	```

2. **Обновите файл `.env`**

	Переименуйте `.env.example` в `.env` и обновите его согласно вашим настройкам

3. **Соберите и запустите Docker-контейнеры**

	```bash
	cd project-folder
	```
	```bash
	docker compose -f docker/docker-compose.yml --env-file .env up --build
	```

## Использование
- API будет доступен по адресу: http://localhost:8000
- Для взаимодействия с API используйте Swagger UI: http://localhost:8000/docs

## Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).
