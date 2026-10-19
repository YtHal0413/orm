# Questão 3.2
from datetime import date
from modelos_escola import Base, Aluno, Turma
from sqlalchemy import create_engine, exists, select, or_, func
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

with Session() as session:
    aluno1 = Aluno(matricula="2025001", nome="Rômbilo Zenemes", email="rombilo.zenemes@escola.com", data_nascimento=date(2003,5,13), turma_id=1)
    aluno2 = Aluno(matricula="2025002", nome="Lajes Tomeiro", email="lajes.tomeiro@email.com", data_nascimento=date(2004,3,22), turma_id=1)
    turma1 = Turma(nome_turma="Latas Secas", ano_letivo=2025)

    session.add(aluno1)
    session.add(aluno2)
    session.add(turma1)
    session.commit()

    # Questão 4.2
    aluno_get = session.query(Aluno).get(1)
    if aluno_get:
        print(f'Aluno com matricula {aluno_get.matricula} encontrado: {aluno_get.nome}')
    else:
        print("Aluno não encontrado.")

    aluno_all = session.query(Aluno).all()
    for aluno in aluno_all:
        print("////////////////////////////////////////////////")
        print(aluno)

    aluno_alldif = session.execute(select(Aluno)).all()
    if aluno_alldif:
        print("////////////////////////////////////////////////")
        print(aluno_alldif)

    aluno_salldif = session.execute(select(Aluno)).scalars().all()
    for aluno in aluno_salldif:
        print("////////////////////////////////////////////////")
        print(aluno)

    # Questão 5.2
    filtro1 = session.query(Turma).filter_by(nome_turma="3º Ano A").all()
    if filtro1:
        print("////////////////////////////////////////////////")
        print(f'Turma Encontrada: {Turma.id}')
    else:
        print("Turma não encontrada.")    

    filtro2 = session.query(Aluno).filter(or_(Aluno.data_nascimento > date(2005,1,1), Aluno.email.like("%@escola.com"))).all()
    for aluno in filtro2:
        print("////////////////////////////////////////////////")
        print(aluno)

    # Questão 6.2

    filtro3 = session.query(Aluno).filter(exists().where(Aluno.turma_id == 1)).all()
    if filtro3:
        print("////////////////////////////////////////////////")
        print("Turma possui alunos.")
    else:
        print("////////////////////////////////////////////////")
        print("Turma não possui alunos.")

    # Questão 7.2
    print("////////////////////////////////////////////////")
    print(f"Total de Alunos: {session.query(Aluno).count()}")
    print(f"Lista de alunos em ordem alfabética: {[i.nome for i in session.query(Aluno).order_by(Aluno.nome.asc())]}")
    pagina_atual = 2
    tamanho_pagina = 10
    print(f'Lista de Matrículas: {[i.matricula for i in session.query(Aluno).order_by(Aluno.matricula.asc()).limit(tamanho_pagina).offset((pagina_atual - 1) * tamanho_pagina)]}')

    # Questão 8.2
    print("////////////////////////////////////////////////")
    listaalunturma = session.query(Aluno.nome, Turma.nome_turma).outerjoin(Turma).all()
    print(f"Lista de Alunos e suas turmas: {listaalunturma}")
    alunsturm = session.query(Aluno.nome).outerjoin(Turma).filter(Aluno.turma_id == None).all()
    print(f"Lista de Alunos sem turma: {alunsturm}")

    # Questão 9.2
    print("////////////////////////////////////////////////")

    turmAgrup = (
        session.query(Turma.nome_turma, func.count(Aluno.id))
        .join(Aluno)
        .group_by(Turma.nome_turma).having(func.count(Aluno.id) > 30)
        .all()
    )
    for turma, totalAlunos in turmAgrup:
        print(f"Turma: {turma}, total de alunos: {totalAlunos}")

    # Questão 10.2
    print("////////////////////////////////////////////////")
    alunos_turma = session.query(Aluno).add_columns((func.current_date() - Aluno.data_nascimento)).all()
    for aluno, idade_aproximada in alunos_turma:
        print(f"Aluno: {aluno.nome}, Idade Aproximada: {idade_aproximada}")
