
from math import sqrt
from math import ceil
from math import floor
# abaixo importa toda biblioteca
#import math # neste caso os comandos devem ter o math.ceil(raiz)

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('a raiz quadrada de {} é {:.2f}'.format(num, raiz))
print('A raiz quadrada de {} arredondada para cima é {}'.format(num, ceil(raiz)))
print('A raiz quadrada de {} arredondada para baixo é {}'.format(num, floor(raiz)))


