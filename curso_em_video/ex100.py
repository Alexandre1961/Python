'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep

def sorteio(lst):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        n = randint(1, 10)
        lst.append(n) # lst passa este valor para numeros
        sleep(0.3)
        print(n, end=' ')
    print('PRONTO!')

def somapar(lst):
    s = 0
    for valor in lst: # para cada valor da lst
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores pares de {lst} temos {s}')


#programa principal
numeros = [] # lista vazia
sorteio(numeros) # passa a lista vazia para a função
somapar(numeros)


