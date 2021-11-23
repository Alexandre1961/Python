'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(v):
    from datetime import date
    ano = date.today().year
    idade = ano - v
    if idade < 16:
        return print(f'Com {idade} anos : NÃO VOTA')
    elif 16 <= idade < 18 or idade >= 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com idade {idade}: VOTO OBRIGATÓRIO.')


ano = int(input('Digite o ano de seu nascimento: '))
voto(ano)

