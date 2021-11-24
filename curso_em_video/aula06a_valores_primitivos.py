#aula06a
#valores primitivos
#int 7, -4, 0, 9873
#float 4.5, 0.076, -15.233, 7.0
#bool True, False
#str 'Ola', '7.5'
#automaticamente o input recebe um valor primitivo str
n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')
soma = n1 + n2
print('n1 é tipo:', type(n1))
print('n2 é tipo:', type(n2))
print('A soma é tipo:', type(soma))
#soma faz uma concatenação das str , n1 + n2
print('A soma e:', soma)
soma = n1 + ' + ' + n2
print('A soma agora é:', soma)
# para resolver isso assuma um valor primitivo int para o input
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print('n1 é tipo: ', type(n1))
print('n2 é tipo: ', type(n2))
print('soma é tipo: ', type(soma))
print('A soma entre', n1,'e', n2,'é: ', soma)
#outra maneira é usar .format()
print ('Usando o syntax {} . format(), fica assim')
print('A soma entre {} e {} é {}'.format(n1, n2, soma))
print('Usando a função float para n1 receber o valor de n1')
n1 = float(n1)
print('Agora n1 é {} e do tipo {} '.format(n1, type(n1)))
