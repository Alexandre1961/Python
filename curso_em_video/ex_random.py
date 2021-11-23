import random
#### RANDOM.RANDOM ####
rr1 = random.random()
print('rr1 = random.random() gera um numero entra 0 e 1 float (0.0, 1.0) ex: {:.3f}'.format(rr1))
#### RANDOM UNIFORME ####
ru = random.uniform(2.5, 4.0)
print('ru = random.uniform(2.5, 3.5 gera um numero aleátorio float entre 2.5 e 3.9999.. ex: {:.3f}'.format(ru)) # Random float:  2.5 <= x < 10.0
#### RANDOM.RANDINT ####
ri = random.randint(3, 5)
print('ri = random.randint(a, b) gera um numero aleátorio int a <= N <= b ex.: randint (3, 5) =  ', ri)
#### RANDOM.RANGE ####
r1 = random.randrange(100)
print('r1= random.randrange(100) gera um numero aleatório entre 0 99 ex.: ', r1) # Random float:  0.0 <= x < 1.0
r2 = random.randrange(90,100)
print('r2 = random.randrange(90,100) gera um numero aleatório entre 90 e 99 ex.: ', r2)
rr = random.randrange(0,101,3)
print('rr = random.randrange(0,100,3) gera um numero aleatorio divisivel por 3 ex.: ', rr)
#### RANDOM.CHOICE ####
lista = ['Ana', 'Paulo', 'Alex', 'Vera']
print('Sendo uma lista com os nome {}, {}, {}, {}'.format(lista[0], lista[1], lista[2], lista[3]))
rc = random.choice(lista)
print('rc = random.choice(lista) retorna um elemento aleatório da lista ex.: {}'.format(rc))# Single random element from a sequence



