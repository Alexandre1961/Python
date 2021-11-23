# leia 3 segmentos de retas e diga se é possivel fazer um triangulo qualquer
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
'''
Simplificando
a + b > c
b + c > a
a + c > b
'''
###
from math import fabs
a = float(input('Qual seg a: '))
b = float(input('Qual seg b: '))
c = float(input('Qual seg c: '))
if fabs(b-c) < b < (a + b) and fabs(a - c) < b < (a + c) and fabs(a - b) < c < (a + b):
    print('Com os segmento {}, {}, {} é possivel montar um triangulo'.format(a, b, c))
else:
    print('')
print('{:#^20}'.format(' MODO SIMPLES '))
if a + b > c and b + c > a and a + c > b:
    print('Estes seguimentos formam um triangulo')
else:
    print('Estes segmentos não formam um triangulo')
print(('{:#^20}'.format(' FIM ')))

