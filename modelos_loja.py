# Questão 2.1, 3.1
from sqlalchemy import Boolean, Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produto (Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    codigo_barras = Column(String(30), unique=True, nullable=False)
    preco = Column(Numeric (10, 2), nullable=False)
    em_estoque = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __repr__(self):
        return f"<Produto(id={self.id}, nome='{self.nome}', codigo_barras='{self.codigo_barras}', preco={self.preco}, em_estoque={self.em_estoque}, categoria_id={self.categoria_id})>"

class Categoria (Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True, nullable=False)

