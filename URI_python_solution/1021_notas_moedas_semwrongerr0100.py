'''Como muitas pessoas, eu tb tava tendo mt dificuldade nessa questão,
pois o input e output estava identico porem eu continuava a receber o "wrong answer 100%" por algum motivo.
O motivo é que o "resto" de todos os calculos, não é zero, e sim um numéro extremamente pequeno,
que seria irrelevante na maioria dos casos, e isso acontece pq a variavel do tipo float tem uma margem de erro muito pequena,
que atrapalha na resolução final do codigo. A solução é trabalhar com números inteiros, utilizando os centavos como base,
ou seja, 100 centavos = 1 real. basta multiplicar o input do tipo float por 100 no começo do código,
e logo em seguida transformar a váriavel do tipo float, em uma do tipo int, e adaptar seus calculos
para trabalhar com os números inteiros.
https://www.urionlinejudge.com.br/judge/pt/questions/view/1021/9464
https://www.youtube.com/watch?v=Z7wZLfZtGHg

use 43,55 e vai sobrar R$ 0.01'''

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    qt_notas = int(round(valor,2)/nota)
    print(f'{qt_notas} nota(s) de R$ {nota:.2f}')
    valor -= qt_notas * nota

print('MOEDAS:')
for moeda in moedas:
    qt_moeda = int(round(valor,2)/moeda)
    print(f'{qt_moeda} moeda(s) de R$ {moeda:.2f}')
    valor -= qt_moeda * moeda
