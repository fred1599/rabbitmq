from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "My Messaging System"
    VERSION: str = "1.0.0"
    RABBITMQ_URL: str = "amqp://guest:guest@localhost/"

settings = Settings()
