# leia um nome de pessoa completo
# informe se ela tem silva no nome
nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome {} tem SILVA? {}'.format(nome, 'SILVA' in nome.upper()))
unome = nome.upper()
print('Seu Nome em maiusculas é: ',unome)
snome = nome.split()
print('Seu nome separado em lista é: ',snome)
print('Existe Silva no nome? {}'.format('SILVA' in snome))

