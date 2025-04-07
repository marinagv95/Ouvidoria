from metodos.operacoes_ouvidoria import registrarManifestacao


def criarManifestacaoMenu(conn):
    while True:
        descricao = input("Descrição da Manifestação: ")
        autor = input("Autor da Manifestação: ")
        ouvidor = input("Ouvidor da Manifestação: ")
        while True:
            tipo = int(input("Tipo da Manifestação ((1) - Reclamação, (2) - Sugestão (3) - Elogio): "))
            if tipo == 1:
                tipo = "Reclamação"
                break
            elif tipo == 2:
                tipo = "Sugestão"
                break
            elif tipo == 3:
                tipo = "Elogio"
                break
            else:
                print(f"Escolha uma opção válida")

        dados = [descricao, autor, ouvidor, tipo]

        if descricao == "" or autor == "" or ouvidor == "" or tipo == "":
            print(f"Dados inválidos!")
        else:
            registroManifestacao = registrarManifestacao(conn, dados)
            print(f"Manifestação registrada com sucesso! - Código: {registroManifestacao} " )
            break

