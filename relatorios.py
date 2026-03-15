import pandas as pd
from bd import conectar

def relatorio_vendas():
    conexao = conectar()
    query = """
    SELECT clientes.nome AS cliente, produtos.nome AS produto, vendas.quantidade, vendas.data_venda
    FROM vendas
    JOIN clientes ON vendas.cliente_id = clientes.id
    JOIN produtos ON vendas.produto_id = produtos.id
    """
    df = pd.read_sql(query, conexao)
    conexao.close()

    print("\nRelatório de Vendas:")
    print(df)

    resumo = df.groupby("cliente")["quantidade"].sum()
    print("\nResumo por cliente:")
    print(resumo)

    return df, resumo 