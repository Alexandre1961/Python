'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    if i < f and p < 0:
        while p < 0:
            p = int(input('PASSO! não pode ser negativo, digite novamente: '))
    if i > f and p > 0:
        while p > 0:
            p = int(input('PASSO não pode ser positivo, digite novamente: '))
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for x in range(i, f, p):
        print(x, end=' ')
        sleep(0.2)
    print(' FIM! ')



#Programa Principal
contador(0, 10, 1)
contador(10, -1, -2)

print('\nAgora é sua vez ce personalizar a contagem: ')
a = int(input('INICIO: '))
b = int(input('FIM: '))
c = int(input('PASSO: '))
contador(a, b, c)

