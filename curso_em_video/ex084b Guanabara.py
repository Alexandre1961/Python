'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

temp = []
prin = []
men = mai = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(prin) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    resp = str(input('Continua S/N '))
    prin.append(temp[:])
    temp.clear()
    if resp in 'Nn':
        break
print('-='*30)
print(f'Foram cadasgrados {len(prin)} pessoas')
print(f'O maior peso foi de {mai}kg de ', end=' ')
for p in prin:
    if p[1] >= mai:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {men}kg de ',end=' ')
for p in prin:
    if p[1] <= men:
        print(f'{p[0]}', end=' ')
