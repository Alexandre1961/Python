cores = {'limpa':'\033[m',
         'amarelo':'\033[4;33m',
         'vermelho':'\033[4;31m',
         'verde':'\033[4;32m',
         'azul':'\033[4;34m',}

nome = str(input('Qual Seu Nome: ')).strip()
if nome.upper() == ('ALEX'):
    print('{}{}{} que nome bonito!'.format(cores ['amarelo'], nome, cores['limpa']))
elif nome.upper() == 'PEDRO' or nome == 'MARIA' or nome == 'JOÂO':
    print('{}{}{}, seu nome é bem popular no Brasil'.format(cores['vermelho'], nome, cores['limpa']))
elif nome.upper() in ('ANA', 'CLAUDIA', 'JESSICA', 'JULIANA'):
    print('{}{}{} é um belo nome feminino.'.format(cores['vermelho'], nome, cores['limpa']))
#else: #opcional
    print('{}{}{} seu nome é bem normal!'.format(cores['verde'], nome, cores['limoa'] ))
print('Tenha um bom dia {}'.format(nome))
