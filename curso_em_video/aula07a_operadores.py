# operadores
r = 9 / 2
ri = 9 // 2
re = 9 % 2
print('9 / 2 = {}, seu inteiro é: {}, e seu resto é {}'.format(r, ri, re))
r = 3 / 1579
ri = 3 // 1579
re = 3 % 1579
print('3 // 1579 = {}, seu interiro é: {}, e seu resto é {}'.format(r, ri, re))
r = 1600 ** 1500
print('1600 ** 1500 = {}'.format(r))
# fução potencia pow
r = pow(4, 3)
print('pow(4,3) = {}'.format(r))
r = 81 ** (1/2)
print('r = 81 ** (1/2) = {}'.format(r))
r = 27 ** (1/3)
print('r = 27 ** (1/3) = {}'.format(r))
#concatenação
r = 'Oi' + 'ola'
#print(''Oi' = 'ola' = {}'.format(r)) synrax error
#mas usando aspas duplas para abrir e fechar
print(" 'Oi' + 'ola' = {} ".format(r))
#repetição
r = 'oi' * 5
#print(''Oi' * 5 = {}'.format(r)) syntax error
print("'Oi' * 5 = {}".format(r))
r = '=' * 20
print(" '=' * 20 = {}".format(r))
nome = input('Qual seu nome? ')
print('Prazer em conhece-lo {}!'.format(nome))
print('Prazer em conhece-lo {:20}!'.format(nome))
print('Prazer em conhece-lo {:>20}!'.format(nome))
print('Prazer em conhece-lo {:<20}!'.format(nome))
print('Prazer em conhece-lo {:^20}!'.format(nome))
print('Prazer em conhece-lo {:=^20}!'.format(nome))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('n1 + n2 = {}'.format(n1+n2))
print('n1 + n2 = {:.3f}'.format(n1+n2))
# para não quebrar a lina entre print
print('Prazer em conhece-lo {}'.format(nome), end=' ! ')
print(' O resultado float.4 entre os dois numeros é {:.04f}'.format(n1 + n2))


