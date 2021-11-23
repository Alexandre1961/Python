'''
faça a tabuada de um numero digitado
usando o laço for
'''
n = int(input('Digite um numero: '))
for i in range(1,11):
    print('{} x {} = {}'.format(n, i, i*n))

