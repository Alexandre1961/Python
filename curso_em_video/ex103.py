'''Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado'''


def ficha(n=0, g=0):
    print(f' O jogador {n} fez {g} gols no campeonato')


#programa principal
nome = str(input('Nome do jogador:'))
gols = str(input('Numero de gols: ')) # se for int e não tiver valor da erro ao teclar enter
if gols.isnumeric():
    gols = int(gols) # transforma g em int
else:
    gols = 0
# resolvido o problema de g ter que ser int, e não informado seja = 0
# resolvemos n sem entrada
if nome.strip() == '': # resolvido se teclando espaço ou apenas ENTER
    nome = '<desconhecido>'
    ficha(nome, gols)
else:
    ficha(nome, gols)



