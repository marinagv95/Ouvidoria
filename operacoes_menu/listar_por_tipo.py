from metodos.operacoes_ouvidoria import buscarManifestacaoTipo


def listarPorTipoMenu(conn):
    while True:
        buscarTipo = int(input("Tipo da Manifestação ((1) - Reclamação, (2) - Sugestão (3) - Elogio): "))
        if buscarTipo == 1:
            buscarTipo = "Reclamação"
            break
        elif buscarTipo == 2:
            buscarTipo = "Sugestão"
            break
        elif buscarTipo == 3:
            buscarTipo = "Elogio"
            break
        else:
            print(f"Escolha uma opção válida")

    dados = [buscarTipo]
    listaPorTipo = buscarManifestacaoTipo(conn, dados)

    if len(listaPorTipo) == 0:
        print(f"Não existe uma Manifestação para o código informado!")
    else:
        for i in listaPorTipo:
            print(f"Código: {i[0]} - Descrição: {i[1]} - Autor: {i[2]} - Ouvidor: {i[3]} - Tipo {i[4]}")