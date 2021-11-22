'''Faça um programa que leia um vetor N[20].
Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc.,
até trocar o 10º com o 11º. Mostre o vetor modificado.
Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.
Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.'''

N = []

for i in range(0, 20):
    N.append(input())

nova_lista = N[::-1]

for i in range(0, len(nova_lista)):
       print(f"N[{i}] =", nova_lista[i])



