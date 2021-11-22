'''Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda
para organizar os experimentos de um laboratório o qual ela é responsável.
Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório
e o percentual de cada tipo de cobaia utilizada.
Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos.
Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados,
o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.
Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir.
Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas
e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).
Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada
e o percentual de cada uma em relação ao total de cobaias utilizadas,
sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
10
10 C
6 R
15 S
5 C
14 R
9 C
6 R
8 S
5 C
14 R

Total: 92 cobaias
Total de coelhos: 29
Total de ratos: 40
Total de sapos: 23
Percentual de coelhos: 31.52 %
Percentual de ratos: 43.48 %
Percentual de sapos: 25.00 %

'''

qt_testes = int(input())

experimentos = {'C': 0, 'R': 0, 'S': 0}
total_testes = 0

for valor in range(qt_testes):
    qt_animais, cobaia = input().split(' ')
    qt_animais = int(qt_animais)
    total_testes += qt_animais
    experimentos[cobaia] += qt_animais

print(f'''Total: {total_testes} cobaias
Total de coelhos: {experimentos['C']}
Total de ratos: {experimentos['R']}
Total de sapos: {experimentos['S']}
Percentual de coelhos: {experimentos['C']/total_testes *100:.2f} %
Percentual de ratos: {experimentos['R']/total_testes *100:.2f} %
Percentual de sapos: {experimentos['S']/total_testes *100:.2f} %''')
