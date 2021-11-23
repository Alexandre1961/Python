'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
Refaça o DESAFIO 51,
lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
primeiro = int(input('Primeiro: '))
razão = int(input('Razão: '))
numerotermos = int(input('Digite o numero de termos que quer mostrar: '))
contador = 1
while contador <= numerotermos:
    print(primeiro, end=' ')
    primeiro += razão
    contador += 1
print('FIM')


