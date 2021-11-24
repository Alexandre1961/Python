lanche = ('Hanburger', 'Suco', 'Pizza', 'Pudim')
print('1', lanche)
print('    0             1        2       3')
print('   -4            -3       -2      -1')
print('2', lanche[1])
print('3', lanche[-1])
print('4', lanche[1:3]) # pudim não entra
print('5', lanche[2:])
print('6', lanche[1:3])
print('7', lanche[0:3:2])
print('8', lanche[:3])# pudim não entra
print('9', lanche[-3:-1])
print('=-' * 15)
print('for comida in lanche:')
for comida in lanche:
    print(f'No meu lanche tem {comida}')
print('=-' * 15)
print('for pos in range(0, len(lanche)):')
for pos in range(0, len(lanche)):
    print(f'No meu lanche tem {lanche[pos]} na posição {pos}')
print('=-' * 15)
print('for pos, comida in \33[31m enumerate\33[m(lanche): ')
print('\033[31mdevolve em pos a posição da comida e em comida, o nome guardado nesta posição\033[m')
for pos, comida in enumerate(lanche):
    print(f'No meu lanche tem {comida} na posição {pos} ')

print(lanche)
print(sorted(lanche))
numeros = '1', '2', '3', '4', '5', '6', '7', '8', '9'
print(numeros)
print(numeros[0:8:3])

