'''Leia um valor de ponto flutuante com duas casas decimais.
Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01'''

valor = float(input())

nota100 = int(valor/100)
resto100 = valor%100

nota50 = int(resto100/50)
resto50 = resto100%50

nota20 = int(resto50/20)
resto20 = resto50%20

nota10 = int(resto20/10)
resto10 = resto20%10

nota5 = int(resto10/5)
resto5 = resto10%5

nota2 = int(resto5/2)
resto2 = resto5%2

moeda1 = int(resto2/1)
resto1 = resto2%1

moeda_5 = int(resto1/0.5)
resto_5 = resto1%0.5

moeda_25 = int(resto_5/0.25)
resto_25 = resto_5%0.55

moeda_1 = int(resto_25/0.1)
resto_1 = resto_25%0.1

moeda_05 = int(resto_1/0.05)
resto_05 = resto_1%0.5

moeda_01 = int(resto_05/0.01)

print(f'''NOTAS:
{nota100} nota(s) de R$ 100.00
{nota50} nota(s) de R$ 50.00
{nota20} nota(s) de R$ 20.00
{nota10} nota(s) de R$ 10.00
{nota5} nota(s) de R$ 5.00
{nota2} nota(s) de R$ 2.00
MOEDAS:
{moeda1} moeda(s) de R$ 1.00
{moeda_5} moeda(s) de R$ 0.50
{moeda_25} moeda(s) de R$ 0.25
{moeda_1} moeda(s) de R$ 0.10
{moeda_05} moeda(s) de R$ 0.05
{moeda_01} moeda(s) de R$ 0.01''')
