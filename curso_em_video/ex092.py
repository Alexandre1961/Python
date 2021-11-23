'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nasc.: '))
cadastro['idade'] = date.today().year - nasc
cadastro['CTPS'] = int(input('CTPS: ''Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['admissão'] = int(input('Ano de admissão: '))
    cadastro['salario'] = float(input('Salario: R$'))
    cadastro['idaposen'] = cadastro['admissão'] - nasc + 35
print('-='*30)
print(f'Nome tem valor {cadastro["nome"]}')
print(f'Idade tem valor {cadastro["idade"]}')
if cadastro['CTPS'] != 0:
    print(f'CTPS tem valor {cadastro["CTPS"]}')
    print(f'Contratação tem valor {cadastro["admissão"]}')
    print(f'Salario tem valor {cadastro["salario"]}')
    print(f'Aposentadoria tem valor {cadastro["idaposen"]}')
print(f'{" FIM ":&^30}')


