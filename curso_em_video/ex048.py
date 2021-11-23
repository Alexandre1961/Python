'''
programa que mostre os numeros impares
de 1 a 500 e depois
a soma de todos os
multiplos de 3 entre 1 e 500
'''
s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        c += 1
print('A soma dos impares de 1 a 500 divisiveis por 3 é: ', s)
print('Para este resultado foram usados {} numeros'.format(c))
