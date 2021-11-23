'''
\033[style;text;backgroundm
\033{0;33;44m
style
0 nenhum
1 Bold
4 Underline
7 negative
numero cores de texto  cores de fundo
30      branco          40 branco
31      vermeho         41 vermelho
32      verde           42 verde
33      amarelo         43 amarelo
34      azul            44 azul
35      roxo            45 roxo
36      azul claro      46 azul claro
37      cinza           47 cinza
'''
# código de cores pré definido
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'azul':'\033[34m',}


print('\033[0;30;47m{:$^30}\033[m'.format(' 01 '))
print('\033[4;31;46mOla mundo\033[m')
print('\033[0;30;47m{:$^30}\033[m'.format(' 02 '))
print('\033[4;31;46m$%#@\033[m'*10)
print('\033[0;30;47m{:$^30}\033[m'.format(' 03 '))
print('\033[7;31;47mOla mundo\033[m')
print('\033[0;30;47m{:$^30}\033[m'.format(' 04 '))
print('\033[7;32;44mOla mundo\033[m')
print('\033[0;30;47m{:$^30}\033[m'.format(' 05 '))
print('\033[7;35;44mOla mundo\033[m')
print('\033[0;30;47m{:$^30}\033[m'.format(' 06 '))
print('\033[7;37;44mOla mundo\033[m')
print('\033[0;30;47m{:$^30}\033[m'.format(' 07 '))
print('\033[0;31;40m Ola \033[m\033[4;32;45m Mundo \033[m')
print('\033[0;30;47m{:$^30}\033[m'.format(' 08 '))
nome = 'Alexandre'
sobrenome = 'Carneiro Moreira'
print('Seu nome é {} {} {} e seu sobrenome é {} {} {}'.format('\033[3;32;40m', nome, '\033[m', '\033[7m', sobrenome, '\033[m'))
print('\033[0;30;47m{:$^30}\033[m'.format(' 09 '))
cores = {'limpa':'\033[m', 'amarelo':'\033[33m', 'vermelho':'\033[31m'}
print('seu nome é {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
print('Seu nome é {}{}{} sobrenome {}{}{} !!!'.format(cores['amarelo'], nome, cores['limpa'], cores['vermelho'], sobrenome, cores['limpa'] ))
print('\033[0;30;47m{:$^30}\033[m'.format(' 09 '))
print('\033[7;30mCores preto e branco tem código \033[m')
print(' {:&^20} '.format(' FIM '))

