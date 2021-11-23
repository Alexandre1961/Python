#import math
from math import hypot
co = float(input("Valor do cateto oposto: "))
ca = float(input('Valor do cateto adjacente: '))
#quando usar import Math
#h = math.hypot(ca, co)
h = hypot(ca, co)
print('Em um triangulo e cateto oposto {} e adjacente {} sua hypotenusa é {}'.format(co, ca, h))
h = pow((ca**2 + co**2), (1/2))
print(h)
print('Usando a formula a hipotenusa é {:.2f}'.format(h))


