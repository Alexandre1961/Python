'''
Crie um programa que leia uma frase qualquer
e diga se ela é um palindromo desconsiderando os espaços
A base do teto desaba
'''
from time import sleep
frase = str(input('Digite uma frase: ')).upper()
frase = frase.replace(' ', '')
print(frase)
l = len(frase)
p = ''
for c in range(l, 0, -1):
    p = p + frase[c-1]
print(p)
if frase == p:
    print('A frase é um Palindromo')
else:
    print('A frase não é um Palíndromo')
print('FIM')
# outro comando simples
inverso = frase[::-1]
print('usando frase[::-1] temos: ', inverso)
