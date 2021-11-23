'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o numero da posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
                menor = lista[c]
print(f'A lista que voce digitou foi {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}... ',end='')
