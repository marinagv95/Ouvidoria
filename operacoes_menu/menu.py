from operacoes_menu import *


def menu(conn):
    opcao = -1
    while opcao != 7:
        print(f"\nOpção (1) - 📋 Listagem das Manifestações")
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
            listarPorTipoMenu(conn)

        elif opcao == 3:
            criarManifestacaoMenu(conn)

        elif opcao == 4:
            contarManifestacaoMenu(conn)
        elif opcao == 5:
            buscarManifestacaoCodigoMenu(conn)

        elif opcao == 6:
            excluirManifestacaoMenu(conn)

        elif opcao != 7:
            print(f"Opção inválida!")

    print(f"Obrigado por usar nossos serviços!")
