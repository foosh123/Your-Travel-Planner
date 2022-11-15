from datetime import timedelta
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

PROD_FRONTEND_URL: str = os.getenv("PROD_FRONTEND_URL")
DEV_FRONTEND_URL: str = os.getenv("DEV_FRONTEND_URL")
ENVIRONMENT: str = os.getenv("ENVIRONMENT")
IS_DEV: bool = ENVIRONMENT == "development"
IS_PROD: bool = ENVIRONMENT == "production"
DATABASE_URI = os.getenv("PROD_DB_URL")


FRONTEND_URL: str
if IS_DEV:
    FRONTEND_URL = DEV_FRONTEND_URL
else:
    FRONTEND_URL = PROD_FRONTEND_URL


SECRET_KEY: str = os.getenv("COOKIE_ENCRYPT_SECRET_KEY")
AUTHORIZATION_HEADER: str = "Authorization"
DEFAULT_TIME_DELTA: timedelta = timedelta(days=1)

EMAIL_FROM: str = os.getenv("EMAIL_FROM")
EMAIL_ORG_NAME: str = os.getenv("EMAIL_ORG_NAME")
SENDGRID_API_KEY: str = os.getenv("SENDGRID_API_KEY")
