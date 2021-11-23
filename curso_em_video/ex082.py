'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar S/N')).strip().upper()
    if resp == 'N':
        break
listapar = []
listaimpar = []
for pos, valor in enumerate(lista):
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
print(f'A lista gerada foi : {lista}')
print(f'A lista com os numeros pares é {listapar}')
print(f'A lista com numeros impares é {listaimpar}')
