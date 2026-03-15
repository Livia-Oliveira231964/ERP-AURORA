from bd import conectar

def cadastrar_produto(nome, preco, estoque):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, preco, estoque))
    conexao.commit()
    conexao.close()
    print("Produto cadastrado com sucesso!")