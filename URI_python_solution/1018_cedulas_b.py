'''Leia um valor inteiro.
A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.'''

valor = int(input())
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0
resto = 0 # se não definir dá run time error var not defined

if valor >= 100:
    nota100 = int(valor/100)
    resto = valor % 100
if resto >= 50:
    nota50 = int(resto/50)
    resto = resto % 50
if resto >= 20:
    nota20 = int(resto/20)
    resto = resto % 20
if resto >= 10:
    nota10 = int(resto/10)
    resto = resto % 10
if resto >= 5:
    nota5 = int(resto/5)
    resto = resto % 5
if resto >= 2:
    nota2 = int(resto/2)
    resto = resto % 2
if resto >= 1:
    nota1 = int(resto/1)

print(f'{valor}')
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')
