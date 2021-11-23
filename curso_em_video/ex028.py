xt# faça o computador escolher um numero int de 0 a 5
# peça ao usuário advinhar este numero
# verifique se ele acertou ou errou
from random import randint
from time import sleep
pc = randint(0, 5)
print(pc)
print('-*-'*10)
print('E agora o que eu faço ?')
print('-*-'*10)
vc = int(input('Escolha um numero de 0 a 5 ! '))
print('Processando')
sleep(3)

if pc == vc:
    print('Meus parabéns voce acertou ! pc = {} e vc = {}'.format(pc, vc))
else:
    print('Voce errou ! pc = {} e vc = {}'.format(pc, vc))
print('Até a proxima!')

