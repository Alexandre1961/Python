# faça um programa que leia um ano qualquer  e diga se ele é bissexto
# ano % 4 == 0 True Bissexto
# ano % 4 == 0 and ano % 100 != 0 True Bissexto
# ano % 4 == 0 and ano % 100 == 0 and ano % ==0 True Bissexto
from datetime import date
ano = int(input('Digite um ano ou 0 para pegar o ano atual do pc: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
print('{:&^20}'.format(' THE END '))