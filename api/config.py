from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LOG_LEVEL: str
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: str = "6379"
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    DOMAIN: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()


broker_url = Config.REDIS_URL
result_backend = Config.REDIS_URL
broker_connection_retry_on_startup = True
