'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
'''
jogador  = {}
listagols = []
cont = 0
jogador['nome'] = str(input("nome: "))
qtpartidas = int(input('Quantas partidas ele jogou: '))
for c in range(0, qtpartidas):
    listagols.append(int(input(f"Quantos gols na {c}ª partida: ")))
jogador['gols'] = listagols[:]
jogador['total'] = sum(listagols)
print('-='*30)
print(jogador)
print('-='*30)
print(f'O campo nome tem valor {jogador["nome"]}')
print(f'O campo gols tem valor {listagols}')
print(f'O campo total tem valor {jogador["total"]}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(listagols)} jogos')
for c, v in enumerate(listagols):
    print(f'=> na partida {c} fez {v} gol(s)')
print(f'Foi um total de {jogador["total"]} gol(s)')
