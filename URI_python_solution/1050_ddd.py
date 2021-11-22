ddds = (61, 71, 11, 21, 32, 19, 27, 31)
cidade = ('Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte')

ddd = int(input())

resposta = cidade[ddds.index(ddd)] if ddd in ddds else 'DDD nao cadastrado'
print(resposta)


