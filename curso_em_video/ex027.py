# leia nome completo
# mostre em seguida primeiro e ultimo nome
nome = str(input(('Digite seu nome completo: '))).strip()
lista = nome.split()
print(lista)
comp = len(lista)
print(comp)
print('O primeiro nome é: {}'.format(lista[0]))
#ultimo = (comp // 1 % 10)-1
ultimo = (len(lista) - 1)
print('O ultimo nome é: {}'.format(lista[ultimo]))

#código curto
print('Olá {}, seu primeiro nome é {} e seu ultimo nome é {}'.format(nome, nome.split()[0], nome.split()[-1] ))
