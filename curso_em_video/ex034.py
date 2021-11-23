# calcule o aumento salarial considerando
# acima de R$1250.00 aumento de 10%
# abaixo ou igual disso 15%
sal = float(input('Digite seu salário: '))
if sal <= 1250.00:
    print('Para salário de R${:.2f} seu novo salário é de R${:.2f}'.format(sal, sal * 1.15))
else:
    print('Para o salário de R${:.2f} seu novo salario será de R${:.2f}'.format(sal, sal *1.1))

