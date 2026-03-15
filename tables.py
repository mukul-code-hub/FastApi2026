from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String


metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name",String(50), nullable = False),
    Column("email", String(50),unique=True, nullable = False )
)

def create_tables():
    metadata.create_all(engine)