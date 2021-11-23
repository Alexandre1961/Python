'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.
'''


def fatorial(num, show=False):
    """-> Calcula o fatorial de um numero
    :param num: numero a ser calculado
    :param show: (opcional = False), se True, mostra conta
    :return: resultado do cálculo"""
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show: # entende-se = True
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return f


#programa principal
n = int(input('Digite um numero: '))
print('Fatorial com show = True > ')
print(fatorial(n, True))
# primeiro faz o fatorial / imprime os traços / para depois fazer o return para o print
print('Fatorial s/ param show >\n', fatorial(n))
help(fatorial)

