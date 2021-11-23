'''
mostre na tela todos os numeros pares
que estão no intervalo entre 1 e 50
'''
for c in range(1, 51):
    print('.', end = '')
    if c % 2 == 0:
        print(c, end=' ')
print('fim')

for n in range(2, 51, 2):
    print('.', end = '')
    print(n, end=' ')