'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
0:9:16 '''

minutos = int(input())
hora = minutos//3600
resto = minutos%3600
minuto = resto//60
segundo = resto%60

print(f'{hora}:{minuto}:{segundo}')