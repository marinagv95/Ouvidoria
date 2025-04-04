from metodos.operacoes_ouvidoria import *
def listarManifestacoesMenu(conn):
    todasManifestacoes = listarManifestacoes(conn)

    if len(todasManifestacoes) == 0:
        print(f"Não existem manifestações")

    else:
        for i in todasManifestacoes:
            print(f"Código: {i[0]} - Descrição: {i[1]} - Autor: {i[2]} - Ouvidor: {i[3]} - Tipo {i[4]}")