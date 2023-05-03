from tables import users_table
from connect import engine
from sqlalchemy import update

statement = update(users_table).where(
    users_table.c.name == "Joe"
).values(name="Jerry")


with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()

