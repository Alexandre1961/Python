'''
ESTRUTURA DE REPETIÇÃO COM VARIAVEL DE CONTROLE
'''
for c in range(1, 7):
    print('para frente c= ', c)
print('fim')

for c in range(7, 1, -1):
    print('para traz c= ', c)
print('fim')

for c in range(0, 7, 2):
    print('para frente  pula 2 c= ', c)
print('fim')

for c in range(7, 1, -2):
    print('para traz pula -2 c= ', c)
print('fim')

n = int(input('Digite um numero: '))
for c in range(0, n + 1):
    print('c = {} n = {}'.format(c, n))
print('FIM')

s = 0
for c in range(1, 5):
    print('s = ', s)
    s += c
    print('s += c é: ', s)
i = int(input('inicia em: '))
t = int(input('termina em: '))
p = int(input('pula de : '))
for c in range(i, t + 1, p):
    print('c = ', c)
print('FIM')
