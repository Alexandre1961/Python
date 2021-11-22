'''Pedrinho está organizando um evento em sua Universidade.
O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês.
O problema é que Pedrinho quer calcular o tempo que o evento vai durar,
uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias,
você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”,
seguido de um espaço e o dia do mês no qual o evento vai começar.
Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss.
Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas,
indicando o término do evento.

Exemplo de Entrada	Exemplo de Saída
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.'''

dia = input() # entrada deve ser Dia x
dia = dia.split(' ')
dia_i = int(dia[-1]) * 24 * 60 * 60 # pega a ultima posição que é o dia
horario_i = input().split(' ')
segundos_hi = int(horario_i[0]) * 60 * 60
segundos_mi = int(horario_i[2]) * 60
segundos_i = int(horario_i[4])
segundos_total_i = dia_i + segundos_hi +segundos_mi + segundos_i

dia = input() # entrada deve ser Dia x
dia = dia.split(' ')
dia_f = int(dia[-1]) * 24 * 60 * 60 # pega a ultima posição que é o dia
horario_f = input().split(' ')
segundos_hf = int(horario_f[0]) * 60 * 60
segundos_mf = int(horario_f[2]) * 60
segundos_f = int(horario_f[4])
segundos_total_f = dia_f + segundos_hf + segundos_mf + segundos_f

total_segundos = segundos_total_f - segundos_total_i

dias = int (total_segundos / (24*60*60))
resto_d = int (total_segundos % (24*60*60))
horas = int(resto_d / (60*60))
resto_h = int(resto_d % (60*60))
minutos = int(resto_h / 60)
resto_m = int(resto_h % 60)

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{resto_m} segundo(s)')