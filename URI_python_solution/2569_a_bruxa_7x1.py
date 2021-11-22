'''Dona Clotilde é uma senhora muito simpática que mora em uma vila, na casa 71.
Não se sabe ao certo por que, mas tinha fama de ser bruxa.
Clotilde tinha muita vontade de assistir uma partida de futebol.
Certo dia, ela comprou um líquido para limpar prata e com isto,
ganhou um cupom que dava direito a concorrer a um ingresso para a semifinal da copa do mundo de 2014, no Mineirão,
o jogo entre Alemanha x Brasil.
O sorteio veio e ela ganhou o ingresso.
Clotilde foi ao jogo, o Brasil perdeu de 7 x 1, e todos da vila acharam
que o Brasil tinha perdido daquela forma por causa dela,coitada!
O sobrinho hacker dela, San Tanaz, tomando as dores da tia, resolveu criar um vírus de computador que interferisse
em cálculos matemáticos, de modo que, tudo que envolvesse o número 7 nas contas, se tornaria 0.

Por exemplo:
3 + 4 = 0
33 + 44 = 0
17 + 11 = 21
8 x 9 = 2
12 x 7 = 0
8 + 9 = 10
Entrada
Composto por uma única linha com dois números inteiros a e b ( 0 < a, b < 10000 ),
separados por um operador de soma ou multiplicação.
Saída
Um número inteiro correspondente ao resultado da conta, depois do vírus.'''

a, op, b = input().split(' ')
a = a.replace('7', '0')
b = b.replace('7', '0')

resultado = int(a) + int(b) if op == '+' else int(a) * int(b)
resultado = int(str(resultado).replace('7', '0'))
print(resultado)

