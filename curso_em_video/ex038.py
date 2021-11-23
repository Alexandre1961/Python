'''
programa pede 2 numeros int
escreva se o primeiro é maior que o segundo
se o primeiro é menor que o segundo
ou se são iguais
'''
n1 = int(input('Ecolha o n1: '))
n2  = int(input('Escolha o n2: '))
if n1 > n2:
    print('o numero {} é maior que {} '.format(n1,n2))
elif n1 < n2:
    print('o numero {} é menor que {} '.format(n1, n2))
elif n1 == n2:
    print('O numero {} é igual a {} '.format(n1, n2))
print('{:#^20}'.format(' FIM '))
# OU
if n1 > n2:
    print('o numero {} é maior que {} '.format(n1,n2))
elif n1 < n2:
    print('o numero {} é menor que {} '.format(n1, n2))
else:
    print('O numero {} é igual a {} '.format(n1, n2))
print('{:#^20}'.format(' FIM '))