'''Dona Ricota é uma senhora muito meticulosa.
Como o natal está se aproximando ela quer distribuir pares de presentes para seus familiares.
Durante sua última viagem, Dona Ricota comprou 2n presentes para seus n netos.
Cada presente custou xi reais (1 ≤ i ≤ 2n) e, para evitar conflitos,
ela planeja formar os pares de presentes de modo a minimizar a diferença entre
o valor total do par de presentes mais caro
e o valor total do par mais barato.
Como você é uma pessoa gentil, Dona Ricota resolveu pedir sua ajuda para organizar os presentes.

Entrada
A entrada consiste em vários casos de teste.
A primeira linha de um caso de teste possui um inteiro n (2 ≤ n ≤ 104), a quantidade de netos.
A segunda linha possui 2n inteiros xi (1 ≤ xi ≤ 108, em que 1 ≤ i ≤ 2n)
em ordem decrescente e separados por exatamente um espaço em branco.
Cada inteiro xi representa o valor do i-ésimo presente comprado por Dona Ricota.

A primeira linha do último caso de teste contém n = 0 e não deve ser processada.

Saída
Para cada caso de teste imprima uma linha com o preço total do par de presentes mais caro e o preço total do par de presentes mais barato separados por um espaço em branco.
Exemplo de Entrada	Exemplo de Saída
1
10 10
1
10 5
2
40 39 20 1
4
1090 300 93 82 71 62 53 41
0

20 20
15 15
59 41
1131 153'''


pares = []
tag = 1

while tag != 0:
    num_netos = int(input())

    if num_netos > 0:
        presentes = input().split()
        for i in range(0, num_netos*2):
            presentes[i] = int(presentes[i])

        for i in range(0,num_netos):
            pares.append(presentes[i]+presentes[-i-1])

        maior = max(pares)
        menor = min(pares)
        print(maior, menor)
    else:
        tag = 0



