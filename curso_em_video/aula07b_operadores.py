n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('A some é {}, o produro é {} e a dividão é {:.3f}'.format(s, m, d), end=' - ')
print('A divisão inteira é {}, a potencia é {} e o resto é {} '.format(di, e, r))
print('Soma = {} \nProduto = {}\nA divisão = {:.4} \nDivisão inteira = {} \nPotencia = {} \nResto = {}'.format(s, m, d, di, e, r), end=' <<<>>>')
