'''
Faça um programa que leia 6 valores.
Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
A seguir, mostre a quantidade de valores positivos digitados.
Entrada
Seis valores, negativos e/ou positivos.
Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
4 valores positivos'''
cont = num = 0
for i in range(0, 6):
    num = float(input())
    if num > 0:
        cont += 1
print(f'{cont} valores positivos')
