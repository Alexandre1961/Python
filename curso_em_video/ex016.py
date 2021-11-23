#escolha um numero real ex 6.346
#mostre a parte inteira dele
#veja modulo math
from math import trunc
num = float(input('Digite um numero real ex: x.xxx '))
# para import math use math.trunc
# print('A parte inteira do numero {} é {}'.format(num, math.trunc(num)))
print('A parte inteira do numero {} é {}'.format(num, trunc(num)))
# outra maneira e chamar o int do numero
print('A parte inteira do numero {} é {}'.format(num, int(num)))

