''' Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
n = 0
count = 1
maior = 0
menor = 0
n = int(input('Digite um numero inteiro para começar: '))
menor = maior = n
soma = n
sai = ''
while sai != 'S':
    n = int(input('Digite outro numero inteiro: '))
    count = count + 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    sai = input('Deseja sair s/n: ').strip().upper()
    while sai not in 'SN':
        sai = input('ERRO, s/n').strip().upper()
print('a média é {}, maior é {}, menor é {}'.format(soma/count, maior, menor))
