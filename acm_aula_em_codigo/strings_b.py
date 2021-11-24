print((' Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021)').center(100, ':'))
print(('\033[34m Métodos de string \033[m ').center(100, ':'))
print(('https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods').center(100, ':'))

print(('\033[33m str.capitalize() \033[m').center(100, ':'))
print('''str.capitalize() retorna uma cópia da string com o seu primeiro caractere em maiúsculo e o restante em minúsculo.''')
texto = 'curSO EM videO'
print('texto =  curSO EM videO')
txt = texto.capitalize()
print('txt = texto.capitalize()')
print('txt =>', txt ,', texto =>', texto)

print(('\033[33m str.casefolding() \033[m').center(100, ':'))
print('''mstr.casefolding()é similar a mudar para letras minúsculas,
mas mais agressivo porque destina-se a remover todas as diferenças maiúsculas/minúsculas em uma string.
Por exemplo, a letra minúscula alemã 'ß' é equivalente a "ss".
Como ela já é uma minúscula, o método lower() não irá fazer nada para 'ß';
já o método casefold() converte a letra para "ss".''')
texto = 'cUrSo eM vIdEo'
print('texto =  cUrSo eM vIdEo')
txt = texto.casefold()
print('txt = texto.casefold()')
print('txt =>', txt ,', texto =>', texto)

print(('\033[33m str.center(width[, fillchar]) \033[m').center(100, ':'))
print('''Retorna um texto centralizado em uma string de comprimento width.
Preenchimento é feito usando o parâmetro fillchar especificado (padrão é o caractere de espaço ASCII).
A string original é retornada se width é menor ou igual que len(s).''')
texto = ' CURSO EM VIDEO '
print("texto =  ' CURSO EM VIDEO '")
texto.center(40,'*')
print("texto.center(40,'*') => ",texto.center(40,'*'))

print(('\033[33m str.count(sub[, start[, end]]) \033[m').center(100, ':'))
print('''str.count(sub[, start[, end]])
Retorna o número de ocorrências da sub-string sub que não se sobrepõem no intervalo [start, end].
Argumentos opcionais start e end são interpretados como na notação de fatias.''')
texto = 'CURSO EM VIDEO'
print("texto =  'CURSO EM VIDEO'")
print("texto.count('E', 1, 7) =>", texto.count('E', 1, 7))
print("texto.count('E') =>", texto.count('E'))
print("texto.count('e') =>", texto.count('e'))

print(('\033[33m str.encode(encoding="utf-8", errors="strict") \033[m').center(100, ':'))
print('''Retorna uma versão codificada da string como um objeto bytes.
A codificação padrão é 'utf-8'. errors podem ser fornecidos para definir um esquema de tratamento de erros diferente.''')
texto = ('àgua -  qöo - é - è - ')
print("texto = ('àgua -  qüo - é - è - ')")
txt = texto.encode()
print('txt = texto.encode(), txt => ', txt)

print(('\033[33m str.endswith(suffix[, start[, end]]) \033[m').center(100, ':'))
print('''Retorna True se a string terminar com o suffix especificado,
caso contrário retorna False. suffix também pode ser uma tupla de sufixos para procurar.
Com o parâmetro opcional start, começamos a testar a partir daquela posição.
Com o parâmetro opcional end, devemos parar de comparar na posição especificada.''')
texto = 'CURSO EM VIDEO...wow!!!'
print("texto =  'CURSO EM VIDEO...wow!!!'")
print("          01234567890123456789012")
sufixo = 'wow!!!'
print("sufixo = 'wow!!!'")
print("texto.endswith(sufixo)   ", texto.endswith(sufixo))
print("texto.endswith(sufixo,18)", texto.endswith(sufixo, 18))
sufixo = "SO"
print("sufixo = 'SO'")
print("texto.endswith(sufixo, 0, 4)", texto.endswith(sufixo, 0, 5))
print("texto.endswith(sufixo, 2, 6)", texto.endswith(sufixo, 2, 6))
texto = 'ab\tabc\tabcd\tabc\tab'

print(('\033[33m str.expandtabs(tabsize=8) \033[m').center(100, ':'))
print('''Retorna uma cópia da string onde todos os caracteres de tabulação são substituídos por um ou mais espaços,
dependendo da coluna atual e do tamanho fornecido para a tabulação.
Posições de tabulação ocorrem a cada tabsize caracteres
(o padrão é 8, dada as posições de tabulação nas colunas 0, 8, 16 e assim por diante)''')
print("texto = 'ab\tabc\tabcd\tabc\tab'")
print("'ab\tabc\tabcd\tabc\tab'.expandtabs()  => ", 'ab\tabc\tabcd\tabc\tab'.expandtabs())
print("'ab\tabc\tabcd\tabc\tab'.expandtabs(4) => ", 'ab\tabc\tabcd\tabc\tab'.expandtabs(4))
str = "xyz\t12345\tabc"
print('Original String:', str)
# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))
# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))
# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))
# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))
# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))

print(('\033[33m str.find(sub[, start[, end]]) \033[m').center(100, ':'))
print('''retorna o índice mais baixo na string onde a substring sub é encontrado dentro da fatia s[start:end].
Argumentos opcionais como start e end são interpretados como na notação de fatiamento.
Retorna -1 se sub não for localizado.''')
texto = 'CURSO EM VIDEO...wow!!!'
print("texto =  'CURSO EM VIDEO...wow!!!'")
print("          01234567890123456789012")
print("texto.texto.find('O') indice =>", texto.find('O'))
print("texto.texto.find('O',5,21) indice =>", texto.find('O',5,21))
print("texto.texto.find('DEO') indice =>", texto.find('DEO'))
print("texto.texto.find('cur') indice =>", texto.find('cur'))

print(('\033[33m str.format(*args, **kwargs) \033[m').center(100, ':'))
print("""format() leva 2 argumentos:
o valor a ser formatado
as especificações de como o valor será formatado
[[fill]align][sign][#][0][width][,][.precision][type]
opções:
fill - preenche com        ::=  any character
align - alinhamento        ::=  "<" | ">" | "=" | "^"
signal - sinal             ::=  "+" | "-" | " "
width - comprimento        ::=  inteiro
precision - precisão       ::=  intiro
type - tipo                ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%
""")
print("""Conversor	Significado
d	Inteiro.
i	Inteiro.
f	Float.
F	Float.
o	Inteiros em octal.
x	Inteiros em hexadecimal minuscula
X	Inteiros em hexadecimal maiúsculas
e	Float em formato exponencial minusculo
E	Float em formato exponencial maiúsculo
g	Mesmo que “e” se expoente é maior do que -4 ou inferior a precisão, “f” de outra forma.
G	Mesmo que “E” se expoente é maior do que -4 ou inferior a precisão, “F” de outra forma.
c	Um único caractere.
s	String (converte qualquer objeto python usando str ()).""")
print('d, f and b são tipo')
print('d  é integer')
print('format(123, "d") => ',format(123, "d"))
print('f é float')
print('format(123.4567898, "f") => ', format(123.4567898, "f"))
print('b é binary')
print('format(12, "b") => ',format(12, "b"))
print('preenche com *, alinha o numero a >, use + se positivo,use 10 posições, mostre inteiro')
print('format(1234, "*>+10,d") => ', format(1234, "*>+10,d"))
print('Outros exemplos')
print('format(1234, "$>10,d") => ', format(1234, "$>10,d"))
print('format(1234, "?<+10,d") => ', format(1234, "?<+10,d"))
print('centralize ^, preencha os espaços com 0, use 11 espaços, use float com 2 casas após o ponto')
print('format(123.4567, "^011.2f")', format(123.4567, "^011.2f"))
print('Outros exemplos')
print('format(123.4567, "^015.2f")', format(123.4567, "^015.2f"))
print('format(123.4567, ">020.5f")', format(123.4567, ">020.5f"))
print(''' A string na qual este método é chamado pode conter texto literal
ou campos para substituição delimitados por chaves {}''')
numero = 123
print("numero = 123")
print('a syntax pode ser:')
print("print(f'O numero é {numero:>020.5f}')")
print(f'resultado => {numero:>020.5f}')
print('ou')
print("print('O numero é {:>020.5f}'.format(numero))")
print('resultado => {:>020.5f}'.format(numero))
cidade = 'Parana'
ano = '1961'
mes = 'Março'
dia = '10'
data = '{} , {} de {} de {}'
print(''' Outro exemplo de formatação 
cidade = 'Parana'
ano = '1961'
mes = 'Março'
dia = '10'
data = '{} , {} de {} de {}' ''')
print("print(data.format(cidade, ano, mes, dia))")
print('retorno = ', data.format(cidade, ano, mes, dia))

print(('\033[33m str.format_map(mapping) \033[m').center(100, ':'))
print('''A função format_map () é uma função embutida no Python,
que é usada para retornar o valor de uma chave de dicionário.''')
a = {'nome':'Alexandre', 'sobrenome':'Moreira'}
print("a = {'nome':'Alexandre', 'sobrenome':'Moreira'} ")
print("print('O sobrenome de {nome} é {sobrenome}'.format_map(a)")
print('O sobrenome de {nome} é {sobrenome}'.format_map(a))
print('-'*100)
print(""" profession = {'name': ['Barry', 'Bruce'],
              'profession': ['Engineer', 'Doctor'],
              'age': [30, 31]} """)
profession = {'name': ['Barry', 'Bruce'],
              'profession': ['Engineer', 'Doctor'],
              'age': [30, 31]}
print('-'*100)
print("""print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession))""")
print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession))
print('-'*100)
print("""print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession))""")
print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession))
print('-'*100)
print("""Outro exemplo
n = 10
a = {'nome':"George", 'msg':n}
print('{nome} tem {msg} mensagens novas'.format_map(a))""")
n = 10
a = {'nome':"George", 'msg':n}
print('{nome} tem {msg} mensagens novas'.format_map(a))

print(('\033[33m str.index(sub[, start[, end]]) \033[m').center(100, ':'))
print('''Senelhante a find(), mas levanta ValueError quando a substring não é encontrada.
Argumentos opcionais como start e end são interpretados como na notação de fatiamento.
Retorna -1 se sub não for localizado.''')
texto = 'CURSO EM VIDEO...wow!!!'
print("texto =  'CURSO EM VIDEO...wow!!!'")
print("          01234567890123456789012")
print("texto.index('O') indice =>", texto.index('O'))
print("texto.index('O',5,21) indice =>", texto.index('O', 5, 21))
print("texto.index('DEO') indice =>", texto.index('DEO'))
print('''Neste exemplo o retorno é um erro
print("texto.index('cur') indice =>", texto.index('cur'))
\033[31mTraceback (most recent call last):
  File "D:\............................\strings_b.py", line 201, in <module>
    print("texto.texto.index('cur') indice =>", texto.index('cur'))
ValueError: substring not found \033[m''')

print(('\033[33m str.is?????? \033[m').center(100, ':'))
print("""Todos os metodos a seguir retornam True ou False
n1 = '123'
sp = '  '
a = 'Abc123'
t1 = 'ABC'
t2 = 'Abc Def'
t3 = 'abcd'
ide = 'Ll'""")
n1 = '123'
sp = '  '
a = 'Abc123'
t1 = 'ABC'
t2 = 'Abc Def'
t3 = 'abcd'
ide = 'Ll'
print('n1.isalnum() , são todos numeros ', n1.isalnum())
print('a.isalpha() , são todas letras ', a.isalpha())
print('t3.isascii() , é caracter ascii', t3.isascii())
print('n1.isdecimal() , é decimal ', n1.isdecimal())
print('t1.isdigit() , é um digito ', t1.isdigit())
print('t2.isprintable() , é imprimeivel', t2.isprintable())
print('sp.isspace() , só tem espaços', sp.isspace())
print('t2.istitle() , é um Titulo', t2.istitle())
print('t1.isupper() , são todas maisculas', t1.isupper())
print('t3.islower() , são todas minusculas', t3.islower())
print('ide.isidentifier() é um identificador do python', ide.isidentifier())
print(''' Neste caso as palavras tidas como identificadores são:
Lu - letras maiúsculas
Ll - letras minúsculas
Lt - letras em titlecase
Lm - letras modificadoras
Lo - outras letras
Nl - letras numéricas
Mn - marcas sem espaçamento
Mc - marcas de combinação de espaçamento
Nd - números decimais
Pc - pontuações de conectores
Other_ID_Start - explicit list of characters in PropList.txt to support backwards compatibility
Other_ID_Continue - igualmente''')

print(('\033[33m str.join(iterable) \033[m').center(100, ':'))


