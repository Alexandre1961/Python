'''
programa pergunta o ANO de nascimento de um jovem
responda se não esta na hora de se alistar < 18
se esta na hora de se alistar =18 anos
ou se já passou a hora de se alistar > 18 anos
mostra quanto tempo falta ou quanto tempo passou da hora
'''
from datetime import date
nasc = int(input('Que ano voce nasceu: '))
atual = date.today().year
idade  = atual - nasc
print('Quem nasceu em {} tem {} anos no ano de {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar neste ano de {}'.format(atual))
elif idade < 18:
    falta = 18 - idade
    print('voce não tem 18 anos falta {} anos para o alistamento'.format(falta))
    alistamento = atual + falta
    print('Seu alistamento será no ano de {}'.format(alistamento))
elif idade > 18:
    print('Voce já deveria ter se alistado a {} anos'.format(idade - 18))
    passou = idade - 18
    print('Seu alistamento foi em {}'.format(atual - passou))



