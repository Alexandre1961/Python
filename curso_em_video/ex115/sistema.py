#Vamos criar um menu em Python, usando modularização.

from ex115.layout import menu
from ex115 import cadastro
arquivo = 'pessoas.txt'
if not cadastro.arquivoExiste(arquivo): # se True ok se false não existe
    cadastro.criarArquivo(arquivo)


while True:
    item = menu('Digite sua opção: ')
    if item == 1:
        cadastro.mostra(arquivo)
    elif item == 2:
        cadastro.inclui(arquivo)
    elif item == 3:
        cadastro.altera(arquivo)
    elif item == 4:
        cadastro.exclui(arquivo)
    elif item == 5:
        break