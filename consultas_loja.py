# Questão 3.1
from modelos_loja import Base, Produto, Categoria
from sqlalchemy import create_engine, select, exists, func
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

with Session() as session:
    produto1 = Produto(nome="Mexedor de farinha", codigo_barras="1234567890123", preco=500.00, em_estoque=True, categoria_id=1)
    produto2 = Produto(nome="Mexedor de farinha Gamer", codigo_barras="1234567890124", preco=3500.00, em_estoque=True, categoria_id=1)
    produto3 = Produto(nome="Pote de farinha", codigo_barras="2234567890123", preco=20.00, em_estoque=False, categoria_id=1)
    produto4 = Produto(nome="Pote de farinha Gamer", codigo_barras="2234567890122", preco=50.00, em_estoque=True, categoria_id=1)
    produto5 = Produto(nome="Mouse Gamer", codigo_barras="2234567890142", preco=50.00, em_estoque=True, categoria_id=2)

    categoria1 = Categoria(nome="Utensílios")
    categoria2 = Categoria(nome="Eletrônicos")
    categoria3 = Categoria(nome="Materiais")

    session.add(produto1)
    session.add(produto2)
    session.add(produto3)
    session.add(produto4)
    session.add(produto5)
    session.add(categoria1)
    session.add(categoria2)
    session.add(categoria3)
    session.commit()

    # Questão 4.1
    produto_get = session.query(Produto).get(1)
    if produto_get:
        print("////////////////////////////////////////////////")
        print(f'Produto com ID {produto_get.id} encontrado: {produto_get.nome}')
    else:
        print("////////////////////////////////////////////////")
        print("Produto não encontrado.")

    produto_first = session.query(Produto).first()
    if produto_first:
        print("////////////////////////////////////////////////")
        print(produto_first.nome)

    instrucao = select(Produto)
    produto_sall = session.execute(instrucao).scalars().all()
    for produto in produto_sall:
        print("////////////////////////////////////////////////")
        print(produto)

    # Questão 5.1
    filtro1 = session.query(Produto).filter_by(em_estoque=True).all()
    for produto in filtro1:
        print("////////////////////////////////////////////////")
        print(produto)
    filtro2 = session.query(Produto).filter(Produto.nome.like('%Gamer%'), Produto.preco > 100).all()
    for produto in filtro2:
        print("////////////////////////////////////////////////")
        print(produto)

    # Questão 6.1

    filtro3 = session.query(Produto).filter(exists().where(Produto.categoria_id == 1)).all()
    if filtro3:
        print("////////////////////////////////////////////////")
        print("A categoria possui produtos associados.")
    else:
        print("////////////////////////////////////////////////")
        print("A categoria não possui produtos associados.")
    
    # Questão 7.1
    print("////////////////////////////////////////////////")
    print(f"Total de produtos: {session.query(Produto).count()}")
    print(f"Lista de categorias por produto: {[i.categoria_id for i in session.query(Produto.categoria_id).distinct()]}")
    print(f'Produtos ordenados do mais caro para o mais barato (pg.2): {[i.nome for i in session.query(Produto).order_by(Produto.preco.desc()).limit(5).offset(5)]}')

    # Questão 8.1
    print("////////////////////////////////////////////////")
    listaprodcat = session.query(Produto.nome, Categoria.nome).join(Categoria).all()
    print(f"Lista de produtos e suas categorias: {listaprodcat}")
    catorf = session.query(Categoria.nome).outerjoin(Produto).filter(Produto.id == None).all()
    print(f"Lista de categorias órfãs: {catorf}")

    # Questão 9.1
    print("////////////////////////////////////////////////")

    prodAgrup = (
        session.query(Categoria.nome, func.avg(Produto.preco), func.count(Produto.id))
        .join(Produto)
        .group_by(Categoria.nome).having(func.avg(Produto.preco) > 250)
        .all()
    )
    for categoria, precoMedio, totalProdutos in prodAgrup:
        print(f"Categoria: {categoria}, preço médio: {precoMedio}, total de produtos: {totalProdutos}")

    # Questão 10.1
    print("////////////////////////////////////////////////")
    promo = session.query(Produto).filter(Produto.em_estoque == True).add_columns((Produto.preco * 0.85)).all()
    for produto, precoP in promo:
        print(f"Produto: {produto.nome}, Preço Original: {produto.preco}, Preço Promocional: {precoP}")
