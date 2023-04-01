from bcouvidoria import *

# Conexão com o banco de dados
conn = abrirBancoDados('localhost', 'root', '123456789', 'conta')

while True:
    print("Ouvidoria da Facisa")
    print("1 - Listar reclamações")
    print("2 - Pesquisar reclamação")
    print("3 - Incluir reclamação")
    print("4 - Remover reclamação")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        listarReclamacoes(conn)
    elif opcao == 2:
        pesquisarReclamacao(conn)
    elif opcao == 3:
        incluirReclamacao(conn)
    elif opcao == 4:
        removerReclamacao(conn)
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
