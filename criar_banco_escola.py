# Questão 3.2
from modelos_escola import Base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///escola.db", echo=True)

Base.metadata.create_all(engine)

