s = float(input('O salario atual é : '))
a = float(input('O aumento a ser dado é : '))
print('Salario atual R${} \nAumento de {}% \nNovo salário R${:.2f}'.format(s, a, ((1+(a/100))*s)))
print('Um salário de R${} com {}% de aumento será de R${}'.format(s, a, (s+(s*a/100))))
