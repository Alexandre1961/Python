'''
ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO

for c in range(1,10):
    print(c, end='')
print(' > FIM do for')
c = 1
while c < 10:
    print(c, end='')
    c += 1
print(' > FIM do while')
n=1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
resposta = 's'
while resposta == 's':
    algo = input('Digite algo: ')
    resposta = input('Continua [s/n]: ')
print('FIM')
'''
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Foram digitados {} numeros par e {} numeros impares'.format(par, impar))





