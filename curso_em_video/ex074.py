'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados
e também indique o menor
e o maior valor que estão na tupla.'''
from random import randint
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(numeros)
print(f'O elementos sorteados foram: ')
for elemento in numeros:
    print(f'{elemento}', end=', ')

menor = maior = numeros[0]
for c in numeros[1:len(numeros)+1]:
    if c < menor:
        menor = c
    if c > maior:
        maior = c
print(f'\nO menor elemento é {menor} e o maior elemento é {maior}')
print(f'O maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')
