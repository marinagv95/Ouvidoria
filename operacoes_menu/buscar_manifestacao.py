from metodos.operacoes_ouvidoria import buscarManifestacaoPorCodigo


def buscarManifestacaoCodigoMenu(conn) :
    buscarCodigo = int(input("Digite o código da manifestação: "))
    dados = [buscarCodigo]
    buscarManifestacaoCodigo = buscarManifestacaoPorCodigo(conn, dados)
    if len(buscarManifestacaoCodigo) == 0:
        print(f"Código da manifestação inválido!")
    else:
        print(
            f"O código da manifestação: {buscarManifestacaoCodigo[0][0]} -  Manifestação: {buscarManifestacaoCodigo[0][1]} - Autor: {buscarManifestacaoCodigo[0][2]}")