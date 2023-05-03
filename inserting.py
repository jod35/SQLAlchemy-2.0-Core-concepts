from sqlalchemy import insert
from tables import users_table
from connect import engine

statement = insert(users_table)

with engine.connect() as conn:
    conn.execute(statement,[
        {'name':"Joe","fullname":"Joe Biden"},
        {'name':"Sponge","fullname":"Sponge Bob"}
    ])
    conn.commit()