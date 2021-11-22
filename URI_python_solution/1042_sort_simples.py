'''Leia 3 valores inteiros e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente,
uma linha em branco e em seguida, os valores na sequência como foram lidos.
7 21 -14

-14
7
21

7
21
-14'''
from typing import List
'''
lista: list[int] = input().split()
URI
Traceback (most recent call last):
  File "Main.py", line 8, in 
    lista: list[int] = input().split()
TypeError: ******* object is not subscriptable

não é iniciante
#lista = [int(x) for x in input().split(" ")]
lista = sorted(lista)
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}\n')
lista_invertida = lista[::-1]
print(f'{lista_invertida[0]}\n{lista_invertida[1]}\n{lista_invertida[2]}')
'''
x = input().split()
a, b, c = x
a = int(a)
b = int(b)
c = int(c)


if a > b and a > c:
    d = a
    if b > c:
        e = b
        f = c
    else:
        e = c
        f = b
if b > a and b > c:
    d = b
    if a > c:
        e = a
        f = c
    else:
        e = c
        f = a
if c > a and c > b:
    d = c
    if a > b:
        e = a
        f = b
    else:
        f = a
        e = b
print(f)
print(e)
print(d)
print()
print(a)
print(b)
print(c)


