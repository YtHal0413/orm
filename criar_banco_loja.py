# Questão 3.1
from modelos_loja import Base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Base.metadata.create_all(engine)