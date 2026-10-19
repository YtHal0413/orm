# Questão 2.2, 3.2
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Aluno (Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    matricula = Column(String(20), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    data_nascimento = Column(Date, nullable=False)
    turma_id = Column(Integer, ForeignKey('turmas.id'), nullable=True)

    def __repr__(self):
        return f"<Aluno(nome='{self.nome}', matricula='{self.matricula}')>"

class Turma (Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True)
    nome_turma = Column(String(50), unique=True, nullable=False)
    ano_letivo = Column(Integer, nullable=False)
