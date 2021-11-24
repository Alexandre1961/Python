def textoFormatado(txt):
    """
    print 1 linha de '?'* comp
    comp = len(txt)+10 espaços
    Centraliza txt em comp
    Coloca txt em Upper Case
    print outra linha de '?'* comp
    :param txt: Texto a ser passado
    :return: none
    """
    comp = len(txt)+10
    txt = txt.upper()
    print('?'*comp)
    print(txt.center(comp).upper())
    print('?' * comp)

def texto(txt):
    print(txt*30)

def soma(a=0, b=0, c=0):
    """
    Soma 3 valores opcionais
    :param a: opcional
    :param b: opcional
    :param c: opcional
    :return:
    """
    s = a + b + c
    print(f'Soma de {a}+{b}+{c}={s}')



textoFormatado(' Help nas funções ')
print('Chamando help(textoFormatado) temos:')
help(textoFormatado)
texto('-=')
print('Chamando def soma() onde a,b,c são obrigatorios')
print('def soma (a, b, c ):')
soma(2, 4, 5)
texto('=-')
print('Chamando def soma() onde c é opcional')
print('def soma (a, b, c=0):')
soma(2, 4, 5)
soma(2, 4)
texto('-=')
print('Chamando def soma() onde a,b,c são opcionais')
print('def soma (a=0, b=0, c=0):')
soma(2, 4, 5)
soma()
texto('-=')
print('Chamando  soma() onde parametros já são definidos')
print('def soma (c=1,a=2,b=5):')
soma(c=1,a=2,b=5)
texto('-=')




