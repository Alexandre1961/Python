resp = 'S'
num = 0
soma = 0
qt = 0
media = 0
while resp != 'N':
    num = int(input('Digite um numero: '))
    soma += num
    qt += 1
    if qt == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Que continuar s/n ')).strip().upper()
media = soma / qt
print('Acabou, a media é {:.2f}, o maior é {}, o menor é {}'.format(media, maior, menor))
