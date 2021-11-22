'''Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X
Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
Area = XX.X
Entrada
A entrada contém três valores reais.
Saída
O resultado deve ser apresentado com uma casa decimal.'''

a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
perimetro = a+b+c
area = (a+b)/2 * c

if a+b > c and b+c > a and c+a > b:
    print(f'Perimetro = {perimetro:.1f}')
else:
    print(f'Area = {area:.1f}')
