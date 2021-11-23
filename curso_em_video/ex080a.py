'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada por:
primeiro numeros pares ordenados e deposi os numeros impares ordenados:
'''
lista = []
listapar = []
listaimpar = []
qn = int(input('Qual a quantidade numeros quer digitar:'))
for c in range(0, qn):
    n = int(input('Digite o numero: '))
    if n % 2 == 0:
        print(n)
        for chave, valor in enumerate(listapar):
            if n < valor:
                listapar.insert(chave, n)
                break
        else:# grande sacada else finciona com for
            listapar.append(n)
    else:
        for chave, valor in enumerate(listaimpar):
            if n < valor:
                listaimpar.insert(chave, n)
                break
        else:# grande sacada else finciona com for
            listaimpar.append(n)
print('listapar = ', listapar)
print('listaimpar = ', listaimpar)
lista = listapar + listaimpar
print(f'A lista digita foi {lista}')
