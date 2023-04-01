# Importação da biblioteca mysql.connector
import mysql.connector


# Função para abrir a conexão com o banco de dados
def abrirBancoDados(host, user, password, database):
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conn


# Função para listar as reclamações
def listarReclamacoes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reclamacoes")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# Função para pesquisar uma reclamação pelo ID
def pesquisarReclamacao(conn):
    cursor = conn.cursor()
    reclamacao_id = int(input("Digite o ID da reclamação: "))
    cursor.execute("SELECT * FROM reclamacoes WHERE id = %s", (reclamacao_id,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("Reclamação não encontrada.")


# Função para incluir uma nova reclamação
def incluirReclamacao(conn):
    cursor = conn.cursor()
    reclamacao = input("Digite a reclamação: ")
    cursor.execute("INSERT INTO reclamacoes (texto) VALUES (%s)", (reclamacao,))
    conn.commit()
    print("Reclamação adicionada com sucesso!")


# Função para remover uma reclamação pelo ID
def removerReclamacao(conn):
    cursor = conn.cursor()
    reclamacao_id = int(input("Digite o ID da reclamação a ser removida: "))
    cursor.execute("DELETE FROM reclamacoes WHERE id = %s", (reclamacao_id,))
    conn.commit()
    print("Reclamação removida com sucesso!")
