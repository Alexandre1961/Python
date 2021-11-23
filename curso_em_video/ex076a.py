
lista = (('lapis', 1.75), ('borracha', 2),
         ('caderno', 15.90), ('estojo', 25),
         ('transferidor', 4.20), ('compasso', 9.99),
         ('mochila', 120.32), ('canetas', 22.30),
         ('livro', 34.90))
print('-'*60)
print(f'{"LISTA DE PRODUTOS":^60}')
print('-'*60)
for a in lista:
    print(f'{a[0]:.<50}R${a[1]:>8.2f}')
print('-'*60)
print(f'{"fim da lista":^60}')
print('-'*60)