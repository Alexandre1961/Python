'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
'''
item = 0
n1 = int(input('Digite o n1: '))
n2 = int(input('Digite o n2: '))
#while 0 <= item < 5:
while item != 5:
    item = int(input('''Digite uma opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa'''))
    if item > 5:
        print('Opção errada tente novamente.')
        item = 0
    elif item == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}.'.format(n1, n2, soma))
        item = 0
    elif item == 2:
        item = 0
        multiplicar = n1 * n2
        print('A multiplicação de {} x {} é {}.'.format(n1, n2, multiplicar))
    elif item == 3:
        item = 0
        if n1 == n2:
            print('{} = {}, não tem maior'.format(n1, n2))
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
        else:
            print('{} > {}'.format(n2, n1))
    elif item == 4:
        item = 0
        n1 = int(input('Digite o n1: '))
        n2 = int(input('Digite o n2: '))
print('Fim do programa')



