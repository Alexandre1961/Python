'''Escreva um programa que receba o nome de uma sequência de times de futebol
e exiba uma as partidas de um torneio com os times, de forma que:
As partidas devem ser geradas de forma aleatória.
O número de times digitados deve ser par.
O programa deve pedir nomes até que seja digitado “fim” Exemplo:

Entrada:
Digite um time: Flamengo
Digite um time: Vasco
Digite um time: Fluminense
Digite um time: Botafogo
Digite um time: Bangu 2
Digite um time: Barcelona
Digite um time: fim
Barcelona x Botafogo
Saída:
Fluminense x Vasco
Bangu 2 x Flamengo'''

from random import sample

times = []
sorteio_times = []
flag = True

while flag == True:
    time = (input('Digite um numero par de times ou fim para terminar :'))
    times.append(time)
    if time == 'fim' and len(times) % 2 == 1:
        flag =False
        times.remove('fim')
    escolha = sample(times, len(times))
    print(escolha)
for i in range(0,len(escolha)-1):
    print(f'Jogo 1 {escolha[i]} x {escolha[i+1]}')

