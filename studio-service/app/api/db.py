from os import getenv
from dotenv import load_dotenv
from databases import Database
from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)

load_dotenv()

DATABASE_URL = getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

studio = Table(
    'studio', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)

database = Database(DATABASE_URL)
