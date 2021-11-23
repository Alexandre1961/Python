'''Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(* num):
    cont = maior = 0
    print('*'*30)
    print('Analisando os valores')
    for valor in num:
        print(valor, end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores')
    print(f'O maior valor encontrado foi {maior}')


#programa principal
maior(4, 9, 2, 5, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
