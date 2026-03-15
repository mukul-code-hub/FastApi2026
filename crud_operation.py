from db import engine
from tables import users
from sqlalchemy import insert

def create_user(input_name: str, input_email: str):
    with engine.connect() as conn:
        query = insert(users).values(name = input_name, email = input_email)
        conn.execute(query)
        conn.commit()
    
