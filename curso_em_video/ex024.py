# digite um nome de cidade
# diga se este nome começa ou não com 'SANTO'
cidade = str(input('Nome de cidade: ')).strip()
print('A cidade começa com a palavra SANTO? ', cidade[:5].upper() =='SANTO')
