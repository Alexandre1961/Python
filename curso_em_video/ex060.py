'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
n = int(input('Digite um numero inteiro:'))
nr = n
fatorial = n
f = n
print('{}! = {} * {}'.format(fatorial, n, (n - 1)),end='')
while n != 1:
    f = f * (n - 1)
    n -= 1
    if n > 1:
        print(' *', (n-1), end='')
print(' = {}'.format(f))
#usando math
from math import factorial
n = int(input('Digite um numero inteiro:'))
print('Resumindo f = factorial(n) = {}'.format(factorial(n)))
