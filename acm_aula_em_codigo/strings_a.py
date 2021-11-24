print((' Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021)').center(100, ':'))
print(('\033[34m 3.1.2. Strings\033[m ').center(100, ':'))
print(('https://docs.python.org/3/tutorial/introduction.html#strings').center(100, ':'))
print()
print('Muitos exemplos aqui vão mostrar nas linhas do código os seguintes caracteres >>>')
print('Estes exemplos são figuras da tela, rodados no terminal do python')
print('''Comentários dentro do código são ignorados e podem ser feitos com o uso de
cerquilha ou jogo da velha, esse aqui #, antes do texto de comentários ''')
#aqui esta um comentário
#que não será mostrado na tela do terminal
#quando rodar um comando ou teclar enter
#####################################################################################################
print(('\033[31m COMO USAR ASPAS SIMPLES,DUPLAS E ASPAS TRIPLAS \033[m').center(100, '?'))
print("Para definir uma str use ela entre ' ', ex: 'string' ")
print('Voce também pode usar " ", ex: "string"')
print('voce pode usar """ ou'" usar ''' para strings de multiplas linhas")
print('''
''')
print('''Abaixo alguns exemplos de como mostrar strings com  aspas simples ou duplas,  dentro de uma string entre aspas
OBS: As saídas mostram as aspa que encapsulam a string, mais adiante o comando print resolverá isso.

>>> 'spam eggs'  # single quotes
'spam eggs' # a saida mostra as aspas
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.' ''')

print('''
A função print() produz uma saída mais legível, ao omitir as aspas que encapsulam a string
e mostram os caracteres escapados e especiais, porém temos que ter cuidado quando usar \ antes de algumas letras,
mais adiante abordaremos isso :

>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.') # usando o print
"Isn't," they said. # todos os caracteres escapados como aspas são mostrados
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
''')
print(r'''Haverá casos que você irá ter que mostrar strings com estes caracteres,
dentro do comando print, mas não como um new line como mostra o exemplo abaixo,
a solução é o uso de strings raw, colocando a letra r antes da string

>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name''')
print('-'*100)
print('''Observe o código abaixo:
print(""".


Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")''')
print()
print('''Há 3 linhas do ponto após as aspas tripla até começo do texto,
      elas serão incluídas porque no final da cada enter dado já existe um new line, 
      mas se voce colocar barras invertidas nelas, elas eliminam isso ''')
print('-'*100)
print('Print sem barras invertidas')
print(""".


Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print('-'*100)
print('Print com barras invertidas')
print(""".\
\
\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#################################################################################################
print(('\033[31m UNINDO STR COM + E MULTIPLICANDO COM * \033[m').center(100, '?'))
print('Strings podem ser concatenadas (coladas) com o operador +, e repetidas com *')
print('''>>> # 3 times 'un', followed by 'ium'
>>> 3 * ':) ' + '=)'
':) :) :) =)' 
Voce pode optar pela syntax 
>>>
>>> 'Py' 'thon'
'Python'

Porém dá erro se usar variáveis:
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
 O mesmo vale para multiplicar
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax

Se você quiser concatenar variáveis ou uma variável e uma literal, use +:
>>> prefix = 'Py'
>>> prefix + 'thon'
'Python'
''')

print(('\033[31m STRINGS SÃO UM CONJUNTO DE CARACTERES \033[m').center(100, '?'))
print(' Uma string é um conjunto de caracteres e tem sua posição dentro da variável definida da seguinte forma:')
print('nome = PYTHON')
nome = 'PYTHON'
print('PYTHON')
print('012345')
print('Veja esta syntax, nome[2]')
print('Se usada com print irá retornar a posição 2 da string na variável nome, que é T')
print('nome[2] = ', nome[2])
print('-'*100)
print('A contagem das strings também podem ser feitas do ultimo carácter até o primeiro com índices negativos')
print(' P  Y  T  H  O  N')
print('-6 -5 -4 -3 -2 -1')
print('nome[-3] = ', nome[-3])
print('''
Veja estes exemplos:
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[-5]  # character in position -5
'y'
''')
print(('\033[31m FATIAMENTO DE STRINGS \033[m').center(100, '?'))
print('Podemos mostrar pedaços da strings com as seguinte syntax:')
print('''string[i, f, p]
onde:
i => é a posição inicial (\033[4;33mINCLUSA\033[m) a começar o fatiamento, se não indicada será 0

f => é a posição final (\033[4;33mNÃO INCLUSA\033[m) a terminar o fatiamento,
OBS: se maior que o tamanho da str ou não indicado será o final da string

p => é o passo que será mostrado os caracteres, opcional, valendo 1 quando não indicado''')
print('-'*100)
texto = 'CursoEmVideo'
print("texto = 'CursoEmVideo'")
print('         012345678901 entenda 0 após o 9  como 10, e 1 = 11')
print('texto[2:]', texto[2:], '\t=>fatia o texto da posição 2(\033[4;33mINCLUSA\033[m) até o final')
print('          2345678901')
print('texto[:4]', texto[:4], '\t\t\t=>fatia o texto do inicio até a posição 4(\033[4;33mNÃO INCLUSA\033[m)')
print('          01234')
print('Agora observe e endenta estes exemplos.')
print('texto[3:6] => ', texto[3:6])
print('texto[-3:-6] => ', texto[-3:-6])
print('texto[-6:-3] => ', texto[-6:-3])
print('texto[:7:2] => ', texto[:7:2])
print('texto[:3:4] => ', texto[:3:4])
print('texto[4::2] => ', texto[4::2])
print('texto[:7:3] => ', texto[:7:3])
print('texto[3:40] => ', texto[3:40])

print('''
Valores fora do range quando usados em fatiamento são tradados de uma maneira que não geram erros
ou assuma os valores até o do comprimento da string quando usados no argumento final ou passo
''')
print('texto[13:23] => ', texto[13:23])
print('texto[1:11: 30] => ', texto[2:11:30])

print('Porém isso não é valido quando queremos mostrar caracteres em uma determinada posição')
print('''texto[32]\033[31m
Traceback (most recent call last):
File "C:\...........................\strings_a.py" line xxx, in <module>
    print('texto[32]', texto[32])
IndexError: string index out of range \033[m''')
print('-'*100)
print('''strings são imutaveis voce não consegue trocar um caracter dela,
uma vez ela definida voce não consegue alterar nenhuma posição dela como no exemplo abaixo:
>>> texto[0] = 'J' 
\033[31mTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment\033[m
>>> texto[2:] = 'py'
\033[31mTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment\033[m ''')

