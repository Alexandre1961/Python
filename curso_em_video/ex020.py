# de 4 alunos
# faça uma ordem aleatória para ver os trabalhos deles
import random
n1 = 'Alex'
n2 = 'Pedro'
n3 = 'João'
n4 = 'Paulo'
list = [n1, n2, n3, n4]

seq = random.sample([n1, n2, n3, n4],4)
print(seq)

seq = random.sample(list,4)
print(seq)

a1=str(input('Digite o nome 1: '))
a2=str(input('Digite o nome 2: '))
a3=str(input('Digite o nome 3: '))
a4=str(input('Digite o nome 4: '))

alunos=[a1, a2, a3, a4]
ordem=random.shuffle(alunos)
print('A ordem dos alunos é:\n{}'.format(alunos))