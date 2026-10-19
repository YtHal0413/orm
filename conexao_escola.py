# Questão 1.2
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:", echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT sqlite_version()"))
    print (result.scalar())
