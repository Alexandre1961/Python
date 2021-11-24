idade = int(input('Quantos anos tem seu carro: '))
print('Carro novo'if idade <= 3 else 'Carro velho')
print('{:*^20}'.format(' DE NOVO '))
if idade <= 3:
    print('seu carro é novo')
else:
    print('Seu carro é velho')
    print('muito velho')
print('{:=^20}'.format('FIM'))
####################################
nome= str(input('Qual é o seu nome? '))
if nome == 'Alex':
    print('Bonito nome!'.format(nome))
print('Bom dia {}'.format(nome))
if nome == 'PAULO': # se for diferente de Paulo vai para o else
    print('Bonito nome!')
else:
    print('***** NOME SIMPLÓRIO! ****')
print('Bom dia {}'.format(nome))
####################################
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Dgite a natoa 2: '))
m = (nota1 + nota2) / 2
print('A sua média é de: {:.2f}'.format(m))
if m >= 7.0:
    print('Como é  >= 7.0 voce foi aprovado')
else:
    print('Como é < 7.0 voce foi reprovado')
print('Tenha um bom dia')
print('Voce foi aprovado, parabéns'if m >= 7 else'Voce foi reprovado estude mais')
print('Tenha um bom dia')

