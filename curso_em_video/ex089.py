'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
alunos = []
temp = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Nota1: ')))
    temp.append(int(input('Nota2: ')))
    media = (temp[1] + temp[2]) / 2
    temp.append(media)
    print(temp)
    alunos.append(temp[:])
    temp.clear()
    resp = str(input('Continua s/n :'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<5} {"Aluno":<10} {"Média":}')
print('-'*20)
for c, v in enumerate(alunos):
    print(f'{c:<5}{alunos[c][0]:<10}{alunos[c][3]:.1f}')
print('-'*20)
while True:
    item = int(input('Mostrar notas de qual aluno (999 interrompe): '))
    if item == 999:
        break
    print(f'Notas do {alunos[item][0]} são {alunos[item][1]} e {alunos[item][2]}')
print(f'{" VOLTE SEMPRE ":&^40}')
