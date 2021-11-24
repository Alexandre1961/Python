print(f'{" DICIONÁRIO DENTRO DE UMA LISTA / FOR":?^50}')
print("Criando o dicionário estado > estado = {}")
estado = {} # ou estado = dict()
print('Criando uma lista > brasil = []')
brasil = [] # ou brasil = list()
print(f'{" CARREGAR LISTA COM BIBLIOTECAS ":*^50}')
print('for c in range(0,3):')
for c in range(0,3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
print(brasil)
print('Mostrando cada dicionario, for dic in brasil: ')
for dic in brasil:
    print(f'Dicionário : ', dic)
print('\033[0;31mMostrando os dic e seus keys values: \n for k, v in dic.items()\033[m')
for dic in brasil:
    for k, v in dic.items():
        print(f'A chave {k} tem valor {v}')
print()
print('Mostrando cada dicionario, for dic in brasil e ver que tem sigla SP: ')
for p in brasil:
    print(f'o dict atual é {p}') # vai buscar dict item a item
    if p['sigla'] == 'SP': # para o dict atual se sigla = SP
        print(f'{p["sigla"]} no  dict atual e tem uf = {p["uf"]} ') # imprima para o item atual o nome

