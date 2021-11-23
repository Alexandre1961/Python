'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
qt50 = 0
qt20 = 0
qt10 = 0
qt1 = 0

valor = int(input('Qual valor quer sacar: '))
while valor // 50 > 0:
    valor -= 50
    qt50 += 1
    if valor < 50:
        print(f'Voce receberá {qt50} notas de R$50,00.')
while valor // 20 > 0:
    valor -= 20
    qt20 += 1
    if valor < 20:
        print(f'Voce receberá {qt20} notas de R$20,00')
while valor // 10 > 0:
    valor -= 10
    qt10 += 1
    if valor < 10:
        print(f'Voce receberá {qt10} notas de R$10,00')
while valor // 1 > 0:
    valor -= 1
    qt1 += 1
    if valor < 1:
        print(f'Voce receberá {qt1} notas de R$1,00')

print(f'{" VOLTE SEMPRE ":8^40}')


