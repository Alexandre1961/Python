'''
programa le o ano de nascimento de um atleta e informa:
até 9 anos = mirim
até 14 anos = infantil
até 19 anos  = junior
até 25 anos = Senior
acima = master
'''
from datetime import date
atual  = date.today().year
print('O ano é {}'.format(atual))
nasc = int(input('Que ano voce nasceu : '))
idade = atual - nasc
print('Voce nasceu em {}, sua idade é {}'.format(nasc, idade))
if idade <= 9:
    print('Voce tem {}, classe MIRIM'.format(idade))
elif idade <= 14: # se já passou por idade <+9, não precisa 9 < idade <= 14
    print('Voce tem {}, classe INFANTIL'.format(idade))
elif idade <= 19:
    print('Voce tem {}, classe JUNIOR'.format(idade))
elif idade <= 25:
    print('Voce tem {}, classe MASTER'.format(idade))
#else: #também funciona
elif idade > 25:
    print('Voce yem {}, classe SENIOR'.format(idade))
print('{:&^30}'.format(' FIM '))
