'''
---- ANOTAÇÃO POSICIONAL LEVA EM CONTA A POSIÇÃO DE UM NUMERO
SISTEMA DECIMAL 0 1 2 3 4 5 6 7 8 9 0
SISTEMA BINARIO 01
SISTEMA OCTAL 0 1 2 3 4 5 6 7
SISTEMA HEXADECIMAL 0 1 2 3 4 5 6 7
                    8 9 A B C D E F
'''
print('{:&^30}'.format(' BASE OCTAL '))
print('Composta pelos digitos 0 1 2 3 4 5 6 7, não existe 8')
print('   3    7    1')
print('   8^2  8^1  8^0')
print(' 3 * 8^2 + 7 * 8^1 + 1 * 8^0 ')
print(' 3 *  64 + 7 * 8 + 1 * 1')
print('  192   +   56   +  1')
print('  249')
