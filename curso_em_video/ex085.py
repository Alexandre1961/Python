'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''
valores = []
pares = []
impares = []
for n in range(0, 7):
    num = (int(input(f'Digite o {n+1}º valor: ')))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
valores.append(pares[:])
impares.sort()
valores.append(impares[:])
print('-='*30)
print(valores)
print(f'Os valores pares digitados em ordem crescente são {valores[0]}')
print(f'Os valores impares digitados em ordem crescente são {valores[1]}')
