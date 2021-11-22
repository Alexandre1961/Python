'''Leia 5 valores Inteiros.
A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares,
quantos valores digitados foram positivos
e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

Exemplo de Entrada	Exemplo de Saída
-5
0
-3
-4
12

3 valor(es) par(es)
2 valor(es) impar(es)
1 valor(es) positivo(s)
3 valor(es) negativo(s)'''

conta_par = 0
conta_impar = 0
conta_positivo = 0
conta_negativo = 0

for x in range(0, 5):
    num = int(input())
    if num % 2 == 0:
        conta_par += 1
    if num % 2 != 0:
        conta_impar += 1
    if num > 0:
        conta_positivo += 1
    if num < 0:
        conta_negativo += 1

print(f'''{conta_par} valor(es) par(es)
{conta_impar} valor(es) impar(es)
{conta_positivo} valor(es) positivo(s)
{conta_negativo} valor(es) negativo(s)''')

