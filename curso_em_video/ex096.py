'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
 e mostre a área do terreno.'''


def areaTerreno(a, b):
    area = a * b
    print(f'A área de um terreno de {a}X{b} é de {area:.2f}m2')


print(f'{"Controle de Terrenos":^30}')
print('-'*30)
comp = float(input('COMPRIMENTO (m): '))
larg = float(input('LARGURA (m): '))
areaTerreno(comp, larg)
