frase = 'Curso em Video de Python'
print('1', frase.split())
print ('2', frase)
dividido = frase.split()
print('3', dividido)
print('4', dividido[0])
print('5', dividido[2][3])
junto = '-'.join(dividido)
print('6', junto)
frase = 'Curso em Video de Python'
sem = frase.split()
print(sem)
junto = ''.join(sem)
print(junto)
print('Comprimento da str junto = {}'.format(len(junto)))



