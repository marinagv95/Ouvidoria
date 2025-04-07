from operacoes_menu.menu import menu
from operacoesdb import *

conn = criarConexao('127.0.0.1', 'root', 'Psico2022!','ouvidoria')

menu(conn)

encerrarConexao(conn)