# faça um programa que leia um numero de 0 9999 (random)
# e mostre na tela cada um dos digitos separados
# ex se mostrado 1834
# Moste:
# unidade = 4
# dezena = 3
# centena = 8
# milhar = 1
# macete 1245 / 10 = 124.5 seu inteiro é 124 seu resto é 5
# 1245 /

num = float(input('Digite um numero :'))
num = int(num)
u = num // 1
#print(u)
u = u % 10 # resto é a unidade do numero
print('A unidade do numero é: {:5}'.format(u))
d = num // 10
#print(d)
d = d % 10
print('A dezena do numeor é: {:6}'.format(d))
c = num // 100
#print(c)
c = c % 10
print('A centena do numero é: {:5}'.format(c))
m = num // 1000
#print(m)
m = m % 10
print('O milhar do numero é: {:6}'.format(m))


