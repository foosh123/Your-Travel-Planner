import functools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from env_vars import DATABASE_URI

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
