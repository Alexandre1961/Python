'''Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente,
de modo que o lado A representa o maior dos 3 lados.
A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos,
sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.'''

x, y, z = input().split()
x = float(x)
y = float(y)
z = float(z)

if x >= y and x >= z:
    a = x
    if y > z:
        b = y
        c = z
    else:
        b = z
        c = y
if y >= x and y >= z:
    a = y
    if x > z:
        b = x
        c = z
    else:
        b = z
        c = x
if z >= x and z >= y:
    a = z
    if x > y:
        b = x
        c = y
    else:
        b = y
        c = x
if x==y==y==z:
    a=x
    b=y
    c=z

if a < (b + c):
    if a*a == (b*b + c*c):
        print('TRIANGULO RETANGULO')
    if a*a > (b*b + c*c):
        print('TRIANGULO OBTUSANGULO')
    if a*a < (b * b + c * c):
        print('TRIANGULO ACUTANGULO')
    if a==b==c:
        print('TRIANGULO EQUILATERO')
    if a==b!=c or a==c!=b or b==c!=a:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')



