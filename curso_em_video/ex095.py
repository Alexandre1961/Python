''' Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
'''
from time import sleep
jogadores = []
jogador = {}
listagols = []
while True:
    jogador['nome'] = str(input('Nome: '))
    qt = int(input('Quantas partidas ele jogou: '))
    for c in range(0, qt):
        listagols.append(int(input(f'Quantos gols na {c}ª partida ')))
    print(listagols)
    jogador['gols'] = listagols[:] # carrega uma list dentro de um dict
    jogador['total'] = sum(listagols)
    jogadores.append(jogador.copy()) # carrega dict dentro de uma list
    listagols.clear() # limpa a list

    '''while True:
        resp =str(input('Quer continuar S/N '))
        if resp in 'SN':
            break #while True da resp
    if resp == 'N'
        break # sai da inserção de dados'''

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar s/n: ')).strip().upper()[0]# .upper()[0] pega o caracter [0] da resposta
    if resp == 'N':
        break

print('-='*25)
print(f'{"cod":<5}', end='')
for k in jogador.keys(): # como não muda a chave no dict pode usar
    print(f'{k:<20}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Digite o cód do jogador ou (999 para sair): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'O jogador com cod {busca} não existe')
    else:
        print(f'--- DADOS DO JOGADOR {jogadores[busca]["nome"].upper()}')
        for k , v in enumerate(jogadores[busca]['gols']):
            print(f'Na partida {k} ele fez {v} gols')