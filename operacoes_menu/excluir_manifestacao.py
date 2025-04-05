from metodos.operacoes_ouvidoria import removerManifestacaoPorCodigo

def excluirManifestacaoMenu(conn):
    buscarCodigo = int(input("Digite o código para Remoção: "))
    dados = [buscarCodigo]
    linhasAfetadas = removerManifestacaoPorCodigo(conn, dados)

    if linhasAfetadas == 0:
        print(f"Não existe uma Manifestação para o código informado!")
    else:
        print(f"Manifestação Removida com sucesso!")