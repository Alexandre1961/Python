'''Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''
from time import sleep
cores = ['\033[m',       # 0 - limpa
        '\033[0;30;41m', # 1 - vermelho
        '\033[0;30;42m', # 2 - verde
        '\033[0;30;44m', # 3 - azul
        '\033[1;107m',   # 4 - branco
        '\033[;7m',      # 5 - inverte
         ]
def ajuda(txt):
    titulo(f"ASCESSANDO O MANUAL DO COMANDO '{txt}'", 3)
    print(cores[5], end='')
    sleep(2)
    help(txt)


def titulo(msg, cor=0):
    sleep(1)
    comp = len(msg)+10
    print(cores[cor], end='')
    print('~'*comp)
    print(msg.center(comp))
    print('~' * comp)
    print(cores[0], end='') # limpa


#programa principal
resp = ''
while resp != 'Fim':
    titulo('SiSTEMA DE AJUDA PyHELP', 2)
    resp = str((input('\033[mFunção ou biblioteca>'))).strip()
    if resp.upper() == 'FIM':
        break
    else:
        ajuda(resp)
titulo('ATÉ LOGO', 1)

