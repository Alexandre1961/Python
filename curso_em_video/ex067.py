'''
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    print('-=' * 22)
    num = int(input('Digite um numero int para ver sua tabuada: '))
    print('-=' * 22)
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')
print(f'{ " PROGRAMA ENCERRADO " :#^44}')
print('{:&^44}'.format(' PROGRAMA ENCERRADO '))




