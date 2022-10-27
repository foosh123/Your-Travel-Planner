from dotenv import load_dotenv, find_dotenv
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date


load_dotenv(find_dotenv())
POSTGRES_USER: str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")

DATABASE_URI: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/db"
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)
    
    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>"\
                .format(self.title, self.author, self.pages, self.published)

if __name__ == '__main__':
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
