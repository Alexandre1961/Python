import random
import emoji
from time import sleep
figura=[emoji.emojize(':victory_hand:'), emoji.emojize(':raised_hand:'), emoji.emojize(':raised_fist:')]
maquina=random.choice(figura)
print('PEDRA', figura[2])
sleep(1)
print('PAPEL ',figura[1])
sleep(1)
print('TESOURA ', figura[0])