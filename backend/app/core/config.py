from pathlib import Path
from dotenv import load_dotenv
import os

# backend folder
BASE_DIR = Path(__file__).resolve().parents[2]

# .env path
env_file = BASE_DIR / ".env"

print("BASE_DIR:", BASE_DIR)
print("ENV FILE:", env_file)
print("Exists:", env_file.exists())

load_dotenv(dotenv_path=env_file)

class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    )

settings = Settings()

print("HOST =", settings.DB_HOST)
print("PORT =", settings.DB_PORT)