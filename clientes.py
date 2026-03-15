from bd import conectar

def cadastrar_cliente(nome, email, telefone):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, email, telefone))
    conexao.commit()
    conexao.close()
    print("Cliente cadastrado com sucesso!")