'''
crie um programa que jogue
jokempo com voce
pedra papel tesoura
Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).
'''
from time import sleep
from emoji import emojize
from random import randint
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'azul':'\033[34m',}
listacor = ['\033[31m','\033[32m','\033[33m','\033[34m', '\033[35m','\033[36m','\033[37m']
r = randint(0,6)
nome = ['PEDRA', 'TESOURA', 'PAPEL']
figura = [emojize(':victory_hand:'), emojize(':raised_hand:'), emojize(':raised_fist:')]
figuras = figura[0] + figura[1] + figura[2]
print(listacor[r])
print(figuras * 8)
print('{: ^30}'.format(' JO - KEN - PO '))
print(figuras * 8)
print('[0] PEDRA', figura[2], '\n[1] TESOURA',  figura[1], '\n[2] PAPEL', figura[0])
user = int(input('Sua escolha é: '))
print('\033[m')
pc = randint(0, 2)
#print('pc escolheu:', pc)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('\n', figuras * 3, ' JÁ ', figuras * 3, '\n')
sleep(0.5)
if pc == user:
    print(' ' * 4, 'PC {}{}{} x VOCÊ {}{}{}'.format(cores['amarelo'],figura[pc],cores['limpa'], cores['amarelo'],figura[user],cores['limpa']), '\n', ' ' * 5, cores['amarelo'],' EMPATE',cores['limpa'])
elif user > 2:
    print('\33[1;31m OPÇÃO INVALIDA, TENTE NOVAMENTE \033[m')
elif pc == 0 and user == 2:
    print(' ' * 4, 'PC {} x VOCÊ {}{}'.format(figura[pc], cores['verde'], figura[user]), '\n', ' ' * 3, ' VOCÊ VENCEU', cores['limpa'])
elif pc == 1 and user == 0:
    print(' '*4, 'PC {} x VOCÊ {}{}'.format(figura[pc], cores['verde'], figura[user]), '\n', ' ' * 3, ' VOCÊ VENCEU', cores['limpa'])
elif pc == 2 and user == 1:
    print(' ' * 4, 'PC {} x VOCÊ {}{}'.format(figura[pc], cores['verde'], figura[user]), '\n', ' ' * 3, ' VOCÊ VENCEU', cores['limpa'])
else:
    print(' ' * 4, 'PC {}{}{} x VOCÊ {}'.format(cores['verde'], figura[pc], cores['limpa'], figura[user]), '\n', ' ' * 4, cores['verde'], 'PC VENCEU ', cores['limpa'])
print('\n', figuras * 3, ' FIM ', figuras * 3)



