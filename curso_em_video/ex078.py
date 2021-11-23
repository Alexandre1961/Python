'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = []
pmenor = []
pmaior = []
x = ''
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
maior = max(lista)
menor = min(lista)
for p, v in enumerate(lista):
    if v == maior:
        pmaior.append(p)
    if v == menor:
        pmenor.append(p)
print(f'{"":&^45}')
print(f'A lista = {lista}')
print(f'O maior valor é {maior} e esta na posição {pmaior}')
print(f'O menor valor é {menor} e esta na posição {pmenor}')
print(f'{" FIM ":&^45}')
