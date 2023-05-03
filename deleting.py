from tables import users_table
from connect import engine
from sqlalchemy import delete

statement = delete(users_table).where(
    users_table.c.name == "Jerry"
)

with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()