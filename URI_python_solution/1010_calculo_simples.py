'''Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.

Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados.
Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
12 1 5.30
16 2 5.10

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo,
lembrando de deixar um espaço após os dois pontos e um espaço após o "R$".
O valor deverá ser apresentado com 2 casas após o ponto.
VALOR A PAGAR: R$ 15.50'''

cod1, qt1, val1 = input().split(' ') # retorna uma lista=[]
qt1 = int(qt1)
val1 = float(val1)
paga1 = qt1 * val1

cod2, qt2, val2 = input().split(' ')
qt2 = int(qt2)
val2 = float(val2)
paga2 = qt2 * val2

total = paga1 + paga2

print(f'VALOR A PAGAR: R$ {total:.2f}')

