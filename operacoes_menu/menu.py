from operacoes_menu import *


def menu(conn):
    opcao = -1
    while opcao != 7:
        print(f"Opção (1) - 📋 Listagem das Manifestações")
        print(f"Opção (2) - 🏷️ Listagem de Manifestações por Tipo")
        print(f"Opção (3) - 📝 Criar uma nova Manifestação")
        print(f"Opção (4) - 🔢 Exibir quantidade de manifestações")
        print(f"Opção (5) - 🔍 Pesquisar uma manifestação por código")
        print(f"Opção (6) - 🗑️ Excluir uma Manifestação pelo Código")
        print(f"Opção (7) - 🚪 Sair")

        opcao = int(input("\nEscolha uma Opção: "))

        if opcao == 1:
            listarManifestacoesMenu(conn)

        elif opcao == 2:
            print(f"Listagem de Manifestações por Tipo")

        elif opcao == 3:
            criarManifestacaoMenu(conn)

        elif opcao == 4:
            print(f"Exibir quantidade de manifestações")

        elif opcao == 5:
            print(f"Pesquisar uma manifestação por código")

        elif opcao == 6:
            print(f"Excluir uma Manifestação pelo Código")

        elif opcao != 7:
            print(f"Opção inválida!")

    print(f"Obrigado por usar nossos serviços!")

