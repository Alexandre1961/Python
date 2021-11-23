'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
s = input('Qual é o seu sexo [M/F]: ').strip().upper()[0:5]
print('Inputado foi : ', s)
# while s != 'F' and s != 'M':
while s not in 'MF':
    s = input('Digite o valor correto [M/F]: ').upper()[0]
print('Voce é do sexo {}'.format(s))
