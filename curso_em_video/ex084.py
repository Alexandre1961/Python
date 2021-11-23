'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
pessoas = []
cadastro = []
#count = 0 # use o len(cadastro)
mais = menos = 0
while True:
    pessoas.append(str(input('Nome: ').strip().upper()))
    pessoas.append(float(input('Peso:')))
    cadastro.append(pessoas[:])
    pessoas.clear()
    #count += 1 # use o len(cadastro)
    resp = str(input('Continua S/N:'))
    if resp in 'Nn':
        break
print(cadastro)
#print(f'Foram cadastradas {count} pessoas.') # use o len(cadastro)
print(f'Foram cadastradas {len(cadastro)} pessoas')
print('Os maiores pesos foram de: ')
for c,v in enumerate(cadastro):
    if v[1] > 90:
        print(f'{v[0]} de {v[1]}kg')
print('Os menores pesos foram: ')
for c,v in enumerate(cadastro):
    if v[1] < 60:
        print(f'{v[0]} com {v[1]}kg')

