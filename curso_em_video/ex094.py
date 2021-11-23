'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoas = []
dados = {}
soma = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if dados['sexo'] in 'MF':
            break
    pessoas.append(dados.copy())
    resp = str(input('Deseja continuar [S/N]: '))
    while resp not in 'SsNn':
        resp = str(input("Responda apenas S ou N: "))
    if resp in 'Nn':
        break
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f"B) A média de idade é {soma/len(pessoas):5.1f} anos.")
print('C) As mulheres cadastradas são :', end='')
for p in pessoas:
    if p['sexo'] == 'F': # para o dict atual se sexo = f
        print(p['nome'], end= ' ') # imprima para o item atual o nome
print(f'\nD) as pessoas acima da média de idade de {soma/len(pessoas):.2f}são: ')
for dic in pessoas:
    if dic['idade'] > soma/len(pessoas):
        print(f"{dic['nome']} com {dic['idade']} esta acima da media de {soma/len(pessoas):.2f}")
'''
for dic in pessoas:
    if dic['idade'] > soma/len(pessoas):
        print(' ')
        for k, v in dic.items():
            print(f"{k} = {v}",end=' ')
'''