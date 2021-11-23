'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
n = int(input('Digite um numero: '))
f = 1
print('{}! ='.format(n), end=' ')
for n in range(n, 0, -1):
    print('{}'.format(n), end='')
    f *= n
#    print(n, ' x..', end='')
    print(' x ' if n > 1 else ' = ', end='')
print('{}'.format(f))
