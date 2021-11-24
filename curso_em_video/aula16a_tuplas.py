import typing

a = (2, 3, 5, 4)
print(a)
b = (5, 8, 1, 2)
print(b)
c = a + b
print(c)
c = b + a
print('c = ',c)
print(len(c))
print(c.count(5))
print(c)
print('indice de 4 é ', c.index(4))
print('indice de 5 é ', c.index(5))
print('indice de 5 após 1 é', c.index(5, 1))
d = ('a', 'a', 'c', 'a')
e = ('f', 'd', 'a', 'g')
f = d + e
print(' f = ',f)
print('d count ', d.count('a'))
print('f count ', f.count('a'))
print('f[3] é :', f[3])
