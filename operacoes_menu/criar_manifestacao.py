from metodos.operacoes_ouvidoria import registrarManifestacao


def criarManifestacaoMenu(conn):
    while True:
        descricao = input("Descrição da Manifestação: ")
        autor = input("Autor da Manifestação: ")
        ouvidor = input("Ouvidor da Manifestação: ")
        tipo = input("Tipo da Manifestação (Reclamação, Sugestão, Elogio): ").lower()
        dados = [descricao, autor, ouvidor, tipo]

        if descricao == "" or autor == "" or ouvidor == "" or tipo == "":
            print(f"Dados inválidos!")
        elif 'reclamação' in tipo or 'sugestão' in tipo or 'elogio' in tipo:
            registroManifestacao = registrarManifestacao(conn, dados)
            print(f"Manifestação registrada com sucesso! - Código: {registroManifestacao} " )
            break
        elif 'reclamação' not in tipo or 'sugestão' not in tipo or 'elogio' not in tipo:
            print(f"O tipo precisa ser: Reclamação, Sugestão, Elogio")

