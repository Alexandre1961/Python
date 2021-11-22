'''Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
Entrada
O arquivo de entrada contém dois valores inteiros.
Saída
O programa deve imprimir um valor inteiro.
Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
Exemplo de Entrada	Exemplo de Saída
6
-5
5

15
12
13

12
12
0'''

x = int(input())
y = int(input())
soma = 0

if x < y:
    x = x+1
    for n in range(x, y):
        if n % 2 != 0:
            soma = soma + n
else:
    y = y + 1
    for n in range(y, x):
        if n % 2 != 0:
            soma = soma + n
print(soma)
