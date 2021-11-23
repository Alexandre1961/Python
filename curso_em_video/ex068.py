'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
'''
from random import randint
soma = 0
vt = 0
num = 0
while True:
    num = int(input('Digite um numero inteiro: '))
    user = str(input('Ecolha [P] para par ou [I] para impar: ')).strip().upper()
    while user not in 'PI':
        user = input('ERRO - P ou I: ').strip().upper()[0]
    pc = randint(1, 5)
    soma = num + pc
    print(f' PC escolheu {pc} o resto é da soma % 2 = {soma % 2}')
    if soma % 2 == 0 and user == 'P':
        print('Voce venceu')
        vt += 1
        if soma % 2 != 0 and user == 'I':
            print('Voce venceu')
            vt += 1
    else:
        break
print(f'Suas vitorias antes de perder foram {vt}')



