a = [2, 3, 4, 7]
print('lista a = ', a)
b = a
b[2] = 8
print('Quando b[2} = 8 a também recebe 8')
print('b = a , cria um vinculo um vinculo entre a e b.')
print('lista a = ', a)
print('lista b = ', b)
b = a[:]
print('Quando b = a[:], não há vinculo')
b[2] = 9 # como b recebeu os itens de a, não tem vinculo entre eles.
print('lista a = ', a)
print('lista b = ', b)
