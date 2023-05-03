from tables import users_table
from connect import engine
from sqlalchemy import select

statement =  select(users_table).where(users_table.c.name == "Joe")

with engine.connect() as conn:
    result = conn.execute(statement)

    for row in result:
        print(f"<Username= {row.name} fullname={row.fullname}>")


