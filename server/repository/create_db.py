from dotenv import load_dotenv, find_dotenv
import os
import psycopg2


load_dotenv(find_dotenv())

POSTGRES_USER: str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
POSTGRES_CONTAINER_PORT: int = int(os.getenv("POSTGRES_CONTAINER_PORT"))
DATABASE_NAME: str = os.getenv("DB_NAME")

# connection establishment
conn = psycopg2.connect(
   database="postgres",
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host="localhost",
    port=POSTGRES_CONTAINER_PORT
)
  
conn.autocommit = True
  
# Creating a cursor object
cursor = conn.cursor()
  
# query to create a database 
sql = f""" CREATE database {DATABASE_NAME} """
  
# executing above query
cursor.execute(sql)
print(f"Database '{DATABASE_NAME}' created")
  
# Closing the connection
conn.close()

