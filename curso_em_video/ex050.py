'''
programa le 6 numeros inteiros e mostra
a soma dos que forem pares,  se o valor digitado
for impar descarte-0
'''
n = 0
s = 0
for i in range(1,7):
    n = int(input('Digite o {} valor: '.format(i)))
    if n % 2 == 0:
        s += n
print('A soma dos valores pares dentro dos 6 digitados é {}'.format(s))
