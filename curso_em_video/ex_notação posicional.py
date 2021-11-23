print('N O T A Ç Ã O    P O S I C I O N A L')
print('\033[31m{:&^50}'.format(' BASE DECIMAL '))
print('''O numeroS de base decimal ultilizam 10 numeros: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
logo a base decimal é: 
n * 10^3 + n * 10^2 + n * 10^1 + n * 10^0 
o numero 1289 pode ser escrito como :
1 * 1000 + 2 * 100 + 8 * 10 + 9 * 1
1 * 10^3 + 2 * 10^2 + 8 * 10^1 + 9 1^0
\n''')
print('\033[33m{:&^50}'.format(' BASE BINÀRIA '))
print('''O numero de base binario só aceita 0 e 1,
logo a base binária é:
b * 2^3 + b * 2^2 + b * 2^1 + b * 2^0 >>> onde b só pode ser 0 ou 1
o binário 1001 é pode ser escrito como:
1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0 
1 * 8 + 0 * 4 + 0 * 2 + 1 * 1
8 + 0 + 0 + 1
9  = 9[10] \n''')
print('\033[34m{:&^50}'.format(' DECIMAL X BINÀRIA '))
print('''0 = 0       10 = 1010
1 = 1       11 = 1011
2 = 01      12 = 1100
3 = 11      13 = 1101
4 = 100     14 = 1110
5 = 101     15 = 1111
6 = 110     16 = 10000
7 = 111     17 = 10001
8 = 1000
9 = 1001\n
''')
print('\033[34m{:&^50}'.format(' CONVERSÃO DE DECIMAL PARA BINÀRIA '))
print('''numero 13 para binário
[13]10 = 13 | 2  >> 13 dividido por 2 = 2 * 6 resto 1
          1 | 6 | 2 >> 6 dividido por 2 = 2 * 3 resto 1
              0 | 3 | 2  >> 3 dividido por 2 = 2 * 1 resto 1
                  1 | 1 | 2 >> 1 dividido por 2 = 0 * 1 resto 1
                      1 | 0
chegamos ao resultado 0 , pegamos os restos de trás para frente que é :
1 1 0 1 = 13
calculo''')
n = int(input('digite um numero inteiro entre 8  e 15 dois algarismos:'))
bi1 = n // 2
br1 = n % 2
print('inteiro bi1 = ', bi1)
print('resto br1 =', br1)
bi2 = bi1 // 2
br2 = bi1 % 2
print('inteiro bi2= ', bi2)
print('resto = br2', br2)
bi3 = bi2 // 2
br3 = bi2 % 2
print('inteiro bi 3 = ', bi3)
print('resto br3 = ', br3)
bi4 = bi3 // 2
br4 = bi3 % 2
print('inteiro bi4 = ', bi4)
print('resto br4 = ', br4)
print('Numero binario para 13 = {}{}{}{} \n'.format(br4, br3, br2, br1))

'''
analisando o numero 13 base 10
Pot.    16    8    4    2    1
(13)10  __   __   __   __   __
bin     2^4  2^3  2^2  2^1  2^0

quais o numero de potencia
da esquerda para direita

Pot.    16    8    4    2    1
(13)10   0    1    1    0    1
bin     2^4  2^3  2^2  2^1  2^0
que somados dão 13
'''
