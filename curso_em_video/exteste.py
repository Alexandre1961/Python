from math import pow
a, b , c = input().split()
n1 = float(1)
n2 = float(1)
n3 = float(1)
A = float(a)
B = float(b)
C = float(c)
if A >= B and A >= C:
    n1 = A
    if B >= C:
        n2 = B
        n3 = C
    else:
        n2 = C
        n3 = B
if B >= A and B >= C:
    n1 = B
    if A >= C:
        n2 = A
        n3 = C
    else:
        n2 = C
        n3 = A

if C >= A and C >= B:
    n1 = C
    if A >= B:
        n2 = A
        n3 = B
    else:
        n2 = B
        n3 = A

if A == B and B == C:
    n1=A
    n2=B
    n3=C

A = n1
B = n2
C = n3

print(A,' ',B,' ',C)
if A >= (B+C):
    print('NAO FORMA TRIANGULO')
else:
    if pow(A,2) == (pow(B,2) + pow(C,2)):
        print('TRIANGULO RETANGULO')
    if pow(A,2) > (pow(B,2) + pow(C,2)):
        print('TRIANGULO OBTUSANGULO')
    if pow(A,2) < (pow(B,2) + pow(C,2)):
        print('TRIANGULO ACUTANGULO')
    if (A == B == C):
        print('TRIANGULO EQUILATERO')
    if A==B != C or A != B == C or A == C != B:
        print('TRIANGULO ISOSCELES')