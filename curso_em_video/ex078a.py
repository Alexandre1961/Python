'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
maior = max(lista)
xa = lista.index(maior)
xa = str(xa) + '...'
menor = min(lista)
xe = lista.index(menor)
xe = str(xe) + '...'
for p, v in enumerate(lista):
    if v == maior and p != lista.index(maior):
        xa = xa + str(p) + '...'
    if v == menor and p != lista.index(menor):
        xe = xe + str(p) + '...'
print(f'{"":&^45}')
print(f'A lista = {lista}')
print(f'O maior valor é {maior} e esta na posição {xa}')
print(f'O menor valor é {menor} e esta na posição {xe}')
print(f'{" FIM ":&^45}')
