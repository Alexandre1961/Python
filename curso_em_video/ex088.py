'''Faça um programa que ajude um jogador da MEGA SENAa criar palpites.
O programa vai perguntar quantos jogos serão gerados
 e vai sortear 6 números entre 1 e 60 para cada jogo,
 cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
print('-='*15)
print(f'{" JOGO DA LOTERIA ":^30}')
print('-='*15)
loteria = []
temp = []
nj = 0
qj = int(input('Quantas apostas quer fazer: '))
print(f'{"SORTEANDO":^30}')
for c in range(0, qj):
    for n in range(0, 6):
        nj = randint(1, 60)
        if n == 0:
            temp.append(nj)
        else:
            while nj in temp:
                nj = randint(1, 60)
            temp.append(nj)
    loteria.append(temp[:])
    temp.clear()
    sleep(1)
    print(f'Jogo{c+1}: {loteria[c]}')





