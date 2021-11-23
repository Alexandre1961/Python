'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota1: '))
    nota2 = int(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Continuar S/N: '))
    if resp in 'Nn':
        break
print('=-'*20)
print(f'{"No.":<4}{"Nome":<10}{"Media":<8}')
print('-'*26)
for i, v in enumerate(ficha):
    print(f'{i:<4}{v[0]:<10}{v[2]:<8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar nota de qual aluno ( 999 interrompe): '))
    if opc == 999:
        break
    if opc < len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print(f'{" VOLTE SEMPRE ":*^30}')



