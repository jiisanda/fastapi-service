from os import getenv

from databases import Database
from dotenv import load_dotenv
from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, ARRAY)

load_dotenv()

DATABASE_URL = f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/anime_db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

anime = Table(
    'anime',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(255)),
    Column('genres', ARRAY(String)),
    Column('characters', ARRAY(String)),
    Column('studio', ARRAY(String)),
)

database = Database(DATABASE_URL)
