n = 0
soma = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
    print(soma)
print('A soma é : {}'.format(soma))
print(f'A soma é {soma}')
