from random import randint
pc = randint(0, 10)
print(pc)
print('Pensei em um numero:')
tentativas = 0
acertou = False
while acertou == False:
    user = int(input(' digite seu palpite: '))
    tentativas += 1
    if pc == user:
        acertou = True
    else:
        if pc < user:
            print('O numero é menor')
        if pc > user:
            print('O numero e maior')
print('Meu PARABENS {} do pc = ao seu {}, com {} tentativas'.format(pc, user, tentativas))
