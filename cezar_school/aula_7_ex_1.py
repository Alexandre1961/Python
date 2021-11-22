'''Usuario irá infomar o valor do raio, calcule a area da circuferencia
utilizando funções e pi do modulo math.
a. Faça o arredondamento para cima.

b. Faça o arredondamento para baixo.'''


import math as m
raio = float(input('Digite o raio em cm: '))
area = m.pi*pow(raio,2)
print(area)
print(f'Aredondando para cima {m.ceil(area)}')
print(f'Aredondando para baixo {m.floor(area)}')
print(f'Aredondando {area:.2f}')