'''Escreva um programa que implemente o jogo conhecido como pedra, papel, tesoura.
Neste jogo, o usuário e o computador escolhem entre pedra, papel ou tesoura.
Sabendo que:
pedra ganha de tesoura,
papel ganha de pedra
e tesoura ganha de papel,
exiba na tela o ganhador:
usuário ou computador.
Para esta implementação, assuma que o número 0 representa pedra, 1 representa papel e 2 representa tesoura.
O programa deve pedir para o usuário entrar com sua escolha, gerar aleatoriamente a escolha do computador,
 exibir a escolha e indicar o vencedor'''

def verifica(numero):
    if numero > 2 or numero <0:
        numero = int(input("Opções: \n0 - pedra\n1 - papel\n2 - tesoura\nSua escolha: "))
        numero = verifica(numero) # para não ter problema de usar o primeiro numero da pilha
    return numero

from random import randrange
escolha = ('pedra','papel','tesoura')
pc = randrange(1,3)
user = int( input("Opções: \n0 - pedra\n1 - papel\n2 - tesoura\nSua escolha: "))
user = verifica(user)

if user == 0 and pc == 0 or user == 1 and pc == 1 or user == 2 and pc ==2:
    print(f'Empate, user escolheu {escolha[user]} e pc escolheu {escolha[pc]}')
elif user == 0 and pc == 2:
    print(f'O usuario escolheu {escolha[user]} que ganha do pc que escolheu {escolha[pc]}')
elif user == 1 and pc == 0:
    print(f'O usuario escolheu {escolha[user]} que ganha do pc que escolheu {escolha[pc]}')
elif user == 2 and pc == 1:
    print(f'O usuario escolheu {escolha[user]} que ganha do pc que escolheu {escolha[pc]}')
else:
    print(f'O pc escolheu {escolha[pc]} que ganha do user que escolheu {escolha[user]}')

print(user)