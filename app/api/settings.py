from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_USERNAME: str
    REDIS_PASSWORD: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    JWT_ALGORITHM: str = "RS256"

    JWT_PRIVATE_KEY_PATH: str = "/app/api/auth/certs/jwt-private.pem"
    JWT_PUBLIC_KEY_PATH: str = "/app/api/auth/certs/jwt-public.pem"
    JWT_PRIVATE_KEY: str = ""
    JWT_PUBLIC_KEY: str = ""

    PASSWORD_SECRET_KEY_PATH: str = "/app/api/user/certs/secret.key"

    CORS: str

    model_config = SettingsConfigDict(env_file="./.env")


settings = Settings()

with open(settings.JWT_PRIVATE_KEY_PATH, 'r') as key_file:
    settings.JWT_PRIVATE_KEY = key_file.read()

with open(settings.JWT_PUBLIC_KEY_PATH, 'r') as key_file:
    settings.JWT_PUBLIC_KEY = key_file.read()
