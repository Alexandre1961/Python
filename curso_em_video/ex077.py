''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
lista = ('MAria', 'livro', 'apartamento', 'Oceano', 'Restaurante', 'Aviador')
print(lista)
for palavra in lista:
    item = palavra.lower()
    print(item,f'tem {item.count("a")+item.count("e")+item.count("i")+item.count("o")+item.count("u")} vogais')
print(f'{" FIM ":&^30}')