import os
from dotenv import load_dotenv
from enum import Enum
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

class APIConfigEnums(Enum):
    environment = os.getenv("ENVIRONMENT", "development")
    secret_key = os.getenv("SECRET_KEY")
    allowed_hosts = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1 localhost").split(" ")
    engine = os.getenv("SQL_ENGINE", "django.db.backends.sqlite3")
    name = os.getenv("POSTGRES_DB", BASE_DIR / "db.sqlite3")
    user = os.getenv("POSTGRES_USER", "user")
    password = os.getenv("POSTGRES_PASSWORD", "password")
    host = os.getenv("SQL_HOST", "localhost")
    port = int(os.getenv("SQL_PORT", 5432))
    email_host = os.getenv("EMAIL_HOST")
    email_host_user = os.getenv("EMAIL_HOST_USER")
    email_host_password = os.getenv("EMAIL_HOST_PASSWORD")

class CloudinaryConfigEnums(Enum):
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
    api_key = os.getenv("CLOUDINARY_API_KEY")
    api_secret = os.getenv("CLOUDINARY_API_SECRET")