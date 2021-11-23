# 1$ = R$3,27
v = float(input('Quantos reais tem na carteira: '))
r = float(input('US$1.00 vale quantos reais? '))
print('Sendo US$1.00 = R${}, com R${} voce compra R${:.2f}'.format(r, v, v/r))
