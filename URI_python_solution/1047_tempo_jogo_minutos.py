'''Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo.
A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
7 8 9 10
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

7 7 7 7
O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)

7 10 8 9
O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)'''
hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

ht = hf - hi
mt = mf - mi

if ht == 0 and mt == 0:
    ht = 24

if ht == 0 and mt < 0:
    ht = 23
    mt = mt + 60

if ht < 0 and mt == 0:
    ht = ht + 24

if ht < 0 and mt < 0:
    ht = ht + 23
    mt = mt + 60

print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")
