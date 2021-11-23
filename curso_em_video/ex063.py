'''Escreva um programa que leia um número N inteiro qualquer
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8 - 13 - 21 - 34 - 55
                     t1+t2=t3

'''
n =int(input('Quantos termos quer mostar da seq Fibonacci:'))
t1 = 0
t2 = 1
count = 3
print('{} - {}'.format(t1, t2), end='')
while count <= n:
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    print(' - {}'.format(t3), end='')
    count += 1






