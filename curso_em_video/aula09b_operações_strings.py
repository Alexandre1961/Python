frase = 'Curso em Video Python'
print('0', frase.count('y',))
print('1', frase.count('o'))
print('2', frase.count('O'))
print('3', frase.upper().count('O'))
print('4', len(frase))
print('5', frase.capitalize())
print('6', frase.title())
frase = '     Curso em Video Python   '
print('7', frase)
print('8', frase.strip())
frase = '     Curso em Video Python   '
print('9', frase.rstrip(), end='.\n')
print('10', frase.lstrip(), end='.\n')
print('11', frase.replace('Python', 'Android'), end='.\n')
print('12', frase, end='.\n')
frase = frase.replace('Python', 'Android')
print('13',frase)
print('14', frase[0])
frase = frase.strip()
print('15', frase)
print('Curso' in frase)
print('video' in frase)
print('Se existir o trecho rso começa pa posição ', frase.find('rso'))
print('Se existir o video ele começa em', frase.find('video'))
print(frase.lower().find('em'))
frase = 'Ola'
print(frase.find('l',1))


