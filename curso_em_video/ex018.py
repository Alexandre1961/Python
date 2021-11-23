# digite um angulo
# qual o seu seno
# qual seu cosceno
# qual a sua tangente
import math
a = int(input('Digite um angulo: '))
a = math.radians(a)
sen = math.sin(a)
cos = math.cos(a)
tang = math.tan(a)
print('O angulo {} tem seno = {:.2f}, cosceno = {:.2f} e tangente = {:.2f}'.format(a, sen, cos, tang))

from math import radians, cos, sin, tan

an = (float(input('Digite o ângulo da figura:')))
s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))
print(f'Este ângulo tem seu cosseno igual a {c:.2f}', end=' ')
print(f', seno igual a {s:.1f} e tangente igual a {t:.1f}')