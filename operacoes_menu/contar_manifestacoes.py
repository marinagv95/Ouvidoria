from metodos.operacoes_ouvidoria import *


def contarManifestacaoMenu(conn):
    todasManifestacoes = listarQuantidadeDeManifestacoes(conn)

    if len(todasManifestacoes) == 0:
        print(f"Não existem Manifestações")

    else:
        print(f"Exitem um total de {todasManifestacoes[0][0]} ")