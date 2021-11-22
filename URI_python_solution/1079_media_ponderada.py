'''Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir.
Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal.
Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o
primeiro valor tem peso 2,
o segundo valor tem peso 3
e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
3
6.5 4.3 6.2
5.1 4.2 8.1
8.0 9.0 10.0

5.7
6.3
9.3'''

x = int(input())
resultado = []

for i in range(0,x):
    a, b, c = (input()).split()
    a = float(a)*2
    b = float(b)*3
    c = float(c)*5
    media_ponderada = (a + b + c) / (2 + 3 + 5)
    resultado.append(media_ponderada)

for i in range(0,x):
    print(f'{resultado[i]:.1f}')