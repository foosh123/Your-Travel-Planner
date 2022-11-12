from dotenv import load_dotenv, find_dotenv
import functools
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


load_dotenv(find_dotenv())
POSTGRES_USER: str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
POSTGRES_CONTAINER_PORT: int = int(os.getenv("POSTGRES_CONTAINER_PORT"))
POSTGRES_CONTAINER_NAME: str = os.getenv("POSTGRES_CONTAINER_NAME")
DB_NAME: str = os.getenv("DB_NAME")
# DATABASE_URI: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_CONTAINER_PORT}/{DB_NAME}"
DATABASE_URI: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_CONTAINER_NAME}:{POSTGRES_CONTAINER_PORT}/{DB_NAME}"


class BaseRepository:
    engine = create_engine(DATABASE_URI)
    sessionmaker = sessionmaker(bind=engine)
    session: Session = sessionmaker()

    @staticmethod
    def commit_after(func):
        """
        Decorator that commits the session after the function is executed
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            BaseRepository.session.commit()
            return res
        return wrapper
