"""
    Config module
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "GPS Devices Rest API"
    DB_HOST: str ="database"
    DB_NAME: str ="gps_devices"
    DB_PASSWORD: str ="admin"
    DB_PORT: int = 5432
    DB_USER: str ="admin"
    FASTAPI_HOST: str ="localhost"
    FASTAPI_PORT: int = 8000
    HOST_URL: str ="http://localhost:3000"
    POSTGRES_PASSWORD: str ="admin"
    POSTGRES_USER: str ="admin"
    TCP_SERVER_HOST: str ="localhost"
    TCP_SERVER_PORT: int = 5000
    RABBITMQ_HOST: str ="rabbitmq"
    RABBITMQ_PORT: int = 5672
    FAKE_GPS_DEVICE_ID: int = 1


    class Config:
        env_file = ".env"
