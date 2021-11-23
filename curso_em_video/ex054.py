'''
crie um programa que leia o ANO de nascimento de 7 pessoas,
ni final diga que ainda não atingiu a mairoridade e quem já,
maioridade 21 anos
'''
from datetime import date
n1 = input('n1 nasceu = ')
n2 = input('n2 nasceu = ')
n3 = input('n3 nasceu = ')
n4 = input('n4 nasceu = ')
n5 = input('n5 nasceu = ')
n6 = input('n6 nasceu = ')
n7 = input('n7 nasceu = ')
lista = (n1, n2, n3, n4, n5, n6, n7)
print(lista[1])
hoje = date.today().year
print(hoje)
print(lista)
ma = 0
mi = 0
for i in range(0,7):
    if int(hoje) - int(lista[i]) >= 21:
        ma += 1
    else:
        mi += 1
print('Há {} pessoa(s) acima de 21 anos e {} pessoa(s) abaixo'.format(ma, mi))

