[en](README.md) [ru](locale/README.ru.md)

# Fast JWTemplate :rocket:

![GitHub Release](https://img.shields.io/github/v/release/steqa/fast-jwtemplate) ![License](https://img.shields.io/badge/license-MIT-green)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-D02C2A?style=flat&logo=redis&logoColor=white) ![Alembic](https://img.shields.io/badge/Alembic-b57414?style=flat&logo=python&logoColor=white)

## Content
1. [Description](#description)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Setup](#setup)
5. [Usage](#usage)
6. [License](#license)
## Description

This is a template for a FastAPI application with JWT authentication. It uses PostgreSQL for the database and Redis for blacklisting refresh tokens. The project is containerized using Docker.

## Features

- Secure JWT-based user authentication with bcrypt hashing for passwords
- API endpoints for login, logout, and token refresh, with expiration handling
- Blacklisting refresh tokens in Redis for enhanced security
- Creating a user with password validation

## Endpoints

1. **Login User**
	- _**POST**_ `/api/v1/auth/jwt/login`
	- _**Description**_: Authenticates a user and returns an access token and refresh token.
2. **Refresh Token**
	- _**POST**_ `/api/v1/auth/jwt/refresh`
	- _**Description**_: Refreshes the user's JWT access token using the provided refresh token.
3. **Logout User**
	- _**POST**_ `/api/v1/auth/jwt/logout`
	- _**Description**_: Logs out the user by blocking the refresh token.
4. **Create User**
	- _**POST**_ `/api/v1/users`
	- _**Description**_: Creates a new user in the system.
5. **Get Current User**
	- _**GET**_ `/api/v1/users/me`
	- _**Description**_: Retrieves the details of the currently authenticated user.

## Prerequisites

Make sure Docker is installed and running on your system. You can download it from [here](https://www.docker.com/get-started).

## Setup

1. **Clone the repository**

	```bash
	git clone https://github.com/steqa/fast-jwtemplate.git project-folder
	```

2. **Update the `.env` file**

	Rename `.env.example` to `.env` and update with your configuration

3. **Build and start the Docker containers**

	```bash
	cd project-folder
	```
	```bash
	docker compose -f docker/docker-compose.yml --env-file .env up --build
	```

## Usage
- The API will be available at http://localhost:8000
- You can interact with the API using Swagger UI at http://localhost:8000/docs

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
