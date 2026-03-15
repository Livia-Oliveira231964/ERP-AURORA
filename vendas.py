from bd import conectar
from datetime import date

def registrar_venda(cliente_id, produto_id, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    # Verificar estoque
    cursor.execute("SELECT estoque FROM produtos WHERE id = %s", (produto_id,))
    estoque_atual = cursor.fetchone()[0]

    if estoque_atual < quantidade:
        print("Estoque insuficiente!")
        conexao.close()
        return

    # Atualizar estoque
    novo_estoque = estoque_atual - quantidade
    cursor.execute("UPDATE produtos SET estoque = %s WHERE id = %s", (novo_estoque, produto_id))

    # Registrar venda
    sql = "INSERT INTO vendas (cliente_id, produto_id, quantidade, data_venda) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (cliente_id, produto_id, quantidade, date.today()))
    conexao.commit()
    conexao.close()
    print("Venda registrada com sucesso!")