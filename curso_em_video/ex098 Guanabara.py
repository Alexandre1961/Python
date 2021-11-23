'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i > f:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.5)
        print('FIM')
    else:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
            sleep(0.5)
        print('FIM')



#programa principal
contador(0, 10, 1)
contador(10, 0, 2)
print('\nAgora é sua vez ce personalizar a contagem: ')
a = int(input('INICIO: '))
b = int(input('FIM: '))
c = int(input('PASSO: '))
contador(a, b, c)