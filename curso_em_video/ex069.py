'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

over18 = 0
masc = 0
above20 = 0
while True:
    age = int(input('Digite sua idade:'))
    if age > 18:
        over18 += 1
    sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sex == 'M':
        masc += 1
    if sex == 'F' and age < 20:
       above20 += 1
    ask = str(input('Quer continuar [Y/N]: ')).strip().upper()[0]
    if ask not in 'YN':
        ask = str(input('Quer continuar [Y/N]: ')).strip().upper()[0]
    if ask == 'N':
        break
print(f' Foram cadastrados {masc} homens, {above20} mulheres abaixo 20 anos e {over18} pessoas acima dos 18 anos ')
