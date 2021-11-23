'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
print('{:&^38}'.format(' INICIANDO '))
pc = randint(0, 10)
# print(pc)
pontos = 0
while pontos != 13:
    pontos += 1
    sleep(0.3)
    print('{} '.format('.'), end = ' ')
print('\n{:&^38}'.format(' PENSEI EM UM NUMERO ADIVINHE '))
cont = 0
user = 0
if user == pc:
    user = pc +1
while user != pc:
    user = int(input('Adivinhe o numero? '))
    if user != pc:
        print('ERROU ',end='')
    cont += 1
print('\nMEUS PARABENS O NUMERO É {} e voce levou {} vezes para acertar'.format(user, cont))



