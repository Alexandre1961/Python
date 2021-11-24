print(f'{" ABRINDO 2 LISTAS VAZIAS ":*^40}')
dados = list()
composta = []
dados.append('Pedro')#adiciona pedro
dados.append(25)#adiciona 25
print('.append Pedro e 25 em dados', dados)
print(f'{ " VINCULANDO COMPOSTA COM DADOS " :*^40}')
composta.append(dados)
print('composta.append(dados)', composta)
dados[0] = 'Maria'
dados[1] = 18
print('mudando dados [0] e [1] para Maria e 25', dados)
print('composta após alteração em dados', composta)
print('''Composta tem um vinculo com dados
alterando dados mudou composta''')
print(f'{" ABRINDO OUTRAS LISTAS ":*^40}')
teste = []
galera = []
teste.append('Paulo')
teste.append(44)
print('.append Paulo e 44 em teste', teste)
print(f'{" FAZENDO CÓPIA DE TESTE ":*^40}')
galera.append(teste[:])
print('galera.append(teste[:])',galera)
teste[0] = 'Ana'
teste[1] = 33
print('alterando teste para Ana 33', teste)
galera.append(teste[:])
print('galera.append(teste[:])', galera)
