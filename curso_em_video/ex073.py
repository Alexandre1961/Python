'''Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
d) Em que posição está o time da Chapecoense.'''

times = ('Pernaltas','Fuzileiros','PQP FC','Barranco','Quebracoxa','Morro Abaixo','Corrego','Paia Velha','Carroça','Chapecoense','71SC','Pirambeira','Topada','Ranca Toco','Pixaim','Tibuncio','Canelados','Fuim','Azarados','Fura Fila')
print('=-'*30)
print(f'Os cincos primeiros times são {times[:5]}')
print('=-'*30)
print(f'OS ultimos 4 colocasdos são {times[-4:]}')
print('=-'*30)
print(f'Os times em ordem alfabértica são {sorted(times)}')
print('=-'*30)
print('O Chapecoense entá em {}o.'.format(times.index('Chapecoense')+1))
print(f'O Chapecoense esta na {times.index("Chapecoense")+1}ª posição')#  aspas duplas aqui
print(f'{" enumerated(times) ":&^40}')
for pos, times in enumerate(times): # enumerate times devolve pos,nome
    if times == 'Barranco':
        print(f'O {times} esta na pos {pos+1}')
