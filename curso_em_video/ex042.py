'''
leia 3 segmento de retas veja exercicio 35
avise se pode formar um triangulo
se sim diga se ele é
equilatero = 3 lados iguai
isoceles = 2 lados iguais
escaleno = todos os lados diferentes
'''
s1 = int(input('Digite s1: '))
s2 = int(input('Digite s2: '))
s3 = int(input('Digite s3: '))
t = bool(s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2)
print(t)
if t == True and s1 != s2 and s2 != s3 and s3 != s1:
    print('{} != {} != {} triangulo escaleno'.format(s1, s2, s3))
elif t == True and s1 == s2 and s2 == s3 and s3 == s1:
    print('{} = {} = {} triangulo equilatero'.format(s1, s2, s3))
elif t == True:
    print('{}, {}, {} triangulo isoceles'.format(s1, s2, s3))
else:
    print('Os segmentos {}, {}, {}, não formam um triangulo'.format(s1, s2, s3))

# outra maneira
print ('OUTRA MANEIRA')

if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
    print('Os seguimentos acima forma um triangulo', end=' ')
    if s1 == s2 == s3:
        print('EQUILATRERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os segmentos não formam um triangulo')
print('{:&^30}'.format(' FIM '))