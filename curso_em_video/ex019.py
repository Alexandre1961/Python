# do nome de 4 alunos
# escolha um para ajudar o professor
import random
from random import choice
n1 = 'Alex'
n2 = 'Paulo'
n3 = 'Pedro'
n4 = 'João'
lista = [n1, n2, n3, n4]
nr = choice([n1, n2, n3, n4])
print('O escolhido é: {}'.format(nr))
nr = choice(lista)
print('nr é do type {} '.format(type(nr)))
print('O escolhido é: {}'.format(nr))
