'''Faça um programa que tenha uma função chamada escreva()
que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável. '''

def textoFormatado(texto,c):
    comp = len(texto)+c
    print('~'* comp)
    print(texto.center(comp))
    print('~'* comp)


# Programa Principal
txt = str(input('Digite um texto: '))
textoFormatado(txt, 10)
