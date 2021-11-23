'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
estoque = ('lapis', 1.75,
           'borracha', 0.89,
           'caderno', 22.45,
           'estojo', 19.34,
           'regua', 5.14,
           'caneta', 3.40,
           'mochila', 30.00)
print('=-'* 19)
print(f'{" Lista de estoque ":^36}')
print('=-'* 19)
comp_pontos = ''
for pos in range (0,len(estoque)):
    if pos % 2 == 0:
        print(f'{estoque[pos]:.<30}', end='')
    else:
        print(f'R${estoque[pos]:>6}')







