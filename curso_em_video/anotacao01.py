# Aula 7
# Operadores aritimeticos
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
# exponencial 5 elevado a 2
5 ** 2 == 25
# inteiro da divisão
5 // 2 == 2
# resto da divisão
5 % 2 == 1

## precedencia de operadores
#1 () primeiro resolva tudo dentro dos parentesis
#2 ** resolva os exponenciais
#3 * / // % resolva estes do primeiro ao ultimo ( ex se % aparece primeiro na linha faça-o)
#4 + - por ultimo estes

r = 2 + (3**2 + 2/2) * 2 / 10
print(r)
2 + (3**2 + 2/2) * 2 / 10 == 4
r = 3 * 5 + 4 ** 2
print('3 * 5 + 4 ** 2 = ',r)
r = 3 * (5 + 4) ** 2
print('3 * (5 + 4) ** 2 = ',r)



