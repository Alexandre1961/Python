''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
lista = ('Ana', 'livrO', 'apartAmento', 'Oceano', 'RestaurantE', 'AvIador')
print(lista)

for pos in lista:
    print(f'\nA palavra {pos} tem as vogais ',end='')
    for l in pos:
        if l in 'AEIOUaeiou':
            print(l, end='')
print(f'\n{" FIM ":&^30}')
