from operacoesdb import *

def registrarManifestacao(conn, dados):
    registrarmanifestacaoSQL = 'insert into manifestacao(descricao, autor, ouvidor, tipo) values(%s,%s,%s,%s)'
    registrar = insertNoBancoDados(conn, registrarmanifestacaoSQL, dados)

    return registrar

def listarManifestacoes(conn):
    listarManifestacoesSQL= 'select * from manifestacao'
    manifestacoes = listarBancoDados(conn, listarManifestacoesSQL)

    return manifestacoes

def listarQuantidadeDeManifestacoes(conn):
    listarQuantidadeSQL = 'select count(*) from manifestacao'
    quantidade = listarBancoDados(conn, listarQuantidadeSQL)

    return quantidade


def buscarManifestacaoPorCodigo(conn, dados):
    buscarManifestacaoCodigoSQL = 'select * from manifestacao where codigo = %s'
    codigoManifestacao = listarBancoDados(conn, buscarManifestacaoCodigoSQL, dados)

    return codigoManifestacao


def buscarManifestacaoTipo(conn, dados):
    buscarManifestacaoTipoSQL = 'select * from manifestacao where tipo = %s'
    tipo = listarBancoDados(conn, buscarManifestacaoTipoSQL, dados)

    return tipo


def removerManifestacaoPorCodigo(conn, dados):
    removerManifestacaoSQL = 'delete from manifestacao where codigo = %s'
    excluirManifestacao = excluirBancoDados(conn, removerManifestacaoSQL, dados)

    return excluirManifestacao

