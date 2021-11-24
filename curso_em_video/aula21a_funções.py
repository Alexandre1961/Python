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

def teste():
    x = 4
    print(f'Dentro de def teste() n = {n}, porque é uma variavel global')
    print(f'Dentro de def teste() x é declarada e vale {x}')


#programa principal
textoFormatado(' escopo de variaveis ')
print('Declarando n = 2 no programa principal')
n = 2
print(f'n={n} dentro do programa principal')
teste()
print(f'Dentro do programa principal x chamado dá ERRO!\nporque é uma variavél local em def teste()')
texto('-=')


