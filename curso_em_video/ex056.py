'''
Desenvolva um programa que leia:
nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
a média de idade do grupo,
qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.
'''
idadevelho = 0
novas = 0
nomevelho = ''
soma = 0
for i in range(1, 5):
    print('------ {}ª PESSOA ------'.format(i))
    nome = input('Nome: ').strip().upper()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    soma += idade
    if idade > idadevelho and sexo == 'M': # opção sexo in 'Mn', elimina tem que trabalhar com upper()
        idadevelho = idade
        nomevelho = nome
    if idade < 20 and sexo == 'F': # opção sexo in 'Ff', elimina tem que trabalhar com upper()
        novas += 1
print('O sr.{} é o mais velho com {}'.format(nomevelho, idadevelho))
print('Existem {} mulhere(s) com idade abaixo de 20'.format(novas))
print('A média de idade do grupo é de {} anos'.format(soma/4))



