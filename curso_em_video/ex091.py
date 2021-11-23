'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from operator import itemgetter
from time import sleep
print(f'{" VALORES SORTEADOS ":&^35}')
jogo = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
for c, v in jogo.items():
    sleep(1)
    print(f'O {c} tirou {v}')
print(f'{" RANKING DOS JOGADORES ":&^35}')
ranking = []# lista porque o retorno de ranking é uma lista
ranking =sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar, {ranking[k][0]} com {ranking[k][1]}: .')
