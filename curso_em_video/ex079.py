'''Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado, não será adicionado a lista')
    resp = str(input('Sair S/N:')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Sair S/N:')).strip().upper()
    if resp == 'S':
        break
print(f'A lista final é {sorted(lista)}')
print(f'{" FIM ":&^40}')
