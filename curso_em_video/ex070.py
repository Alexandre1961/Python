'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
total = 0
qtacima = 0
valorbarato = 0
nomebarato = ''

while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    valor = float(input('Qual o valor: '))
    if total == 0:
        valorbarato = valor
        nomebarato = produto
    else:
        if valor < valorbarato:
            valorbarato = valor
            nomebarato = produto
    if valor > 1000:
        qtacima += 1
    total += valor # usei esse para pegar o primeiro produto e valor como o mais barato
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Sair [S/N]: ')).strip().upper()[0]
    if resp == 'S':
        break
print(f'{" FIM ":=^30}')
print(f'O total gasto foi de R${total:.2f}')
print(f'{qtacima} produto custaram acima de R$1000.00')
print(f'O produto mais barato foi {nomebarato} no valor de R${valorbarato:.2f}')

