# faça um programa que leia 3 numeros e diga qual o maior e qual o menor
n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
n3 = int(input('Digite n3: '))
print('n1 = {}, n2 = {} n3 = {}'.format(n1,n2,n3))
print('{:#^20}'.format(' Normal '))
if n1 > n2 and n1 > n3:
    print('n1 é o maior')
if n2 > n1 and n2 > n3:
    print('n2 é o maior')
if n3 > n2 and n3 > n1:
    print('n3 é o maior')
if n1 < n2 and n1 < n3:
    print('n1 é o menor')
if n2 < n1 and n2 < n3:
    print('n2 é o menor')
if n3 < n2 and n3 < n1:
    print('n3 é o menor')
# forma de atalho
print('{:#^20}'.format(' ELIMINANDO LINHAS '))
menor = n1 # assume que é menor
if n2 < n1 and n2 < n3: # testa em relação a n2
    menor = n2
if n3 < n1 and n3 < n2: #testa n2 em relação a n3
    menor = n3
print('o menor valor é {}'.format(menor))
print('{:#^20}'.format(' SIMPLIFICADO '))
#forma simplificada
lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))

