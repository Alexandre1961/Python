'''Faça um programa que ajude um jogador da MEGA SENAa criar palpites.
O programa vai perguntar quantos jogos serão gerados
 e vai sortear 6 números entre 1 e 60 para cada jogo,
 cadastrando tudo em uma lista composta.'''
print('-='*20)
print(f'{" JOGO DA MEGA SENNA ":^40}')
print('-='*20)
from random import randint
from time import sleep
jogo = []
jogos = []
qt = int(input('Quantos jogos para sortear: '))
tot = 1
while tot <= qt:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    tot += 1
print('-='*4, f' SORTEANDO {qt} JOGOS ', '-='*4)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(f'{" BOA SORTE ":&^40}')




