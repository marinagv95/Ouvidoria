from operacoes_menu.menu import menu
from operacoesdb import *

conn = criarConexao('127.0.0.1', 'root', 'Bubba724779@','ouvidoria')

menu(conn)

encerrarConexao(conn)