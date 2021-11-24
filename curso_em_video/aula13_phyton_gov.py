'''Numeros primos são divisiveis apenas por um ou por ele mesmo ( 2 divisors ).
Numero 1 só tem 1 vivisor , logo não primo


'''
#r = int(input('Até qual numero quer ver os nº primos: '))
for n in range(2, 50): # procure de 2 ate r
    # começa em  2 de 2, porque 2 é primo
    # 2 de 3, 2 sai para else:, 3 não é par, vai para else:
    # 4 de 2, 4 é par, logo 4 = 2 x 4//2 > os anteriores 2 e 3 vão para else
    #... este for elimina os numeros pares e os divisiveis por outro numero
    # 2 de 9, quando chega em 9, 9 % 3 = 3
     for x in range(2, n): #verifica se o numero é divisivel por algum dos seus antecessores
         if n % x == 0:
             print(f'(n){n} % (x){x} = (resto){n % x}')
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # se não encontrar um fator o loop vem para cá, ex "for 2 de 2", logo 2 é primo
         print(n, 'is a prime number')
