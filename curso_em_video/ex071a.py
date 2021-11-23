ced = 50
totced = 0
valor = int(input('Qual o valor: '))
while True:
    print(f'Vocereceberá {totced} cedulas de R${ced:.2f}')
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        print(f'Vocereceberá {totced} cedulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totced = 0
        if valor == 0:
            break

