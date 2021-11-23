from time import sleep


def aumentar(preço=0, taxa=0, formata=False):
    res = preço + (preço * taxa / 100)
    return res if formata is False else moeda(res)


def diminuir(preço=0, taxa=0, formata=False):
    res = preço - (preço * taxa / 100)
    return res if formata is False else moeda(res)


def dobro(preço=0, formata=False):
    res = preço * 2
    return res if formata is False else moeda(res)

def metade(preço=0, formata=False):
    res = preço / 2
    return res if formata is False else moeda(res)


def moeda(preço, moeda = 'R$'):
    return f'{moeda}{preço:>7.2f}'.replace('.', ',')

def textoFormatado(txt):
    global comp
    comp = len(txt) + 20
    print('-'*comp)
    print(txt.center(comp))
    print('-'*comp)
    # return comp # não funciona


def resumo(preço=0, a=0, b=0):
    textoFormatado(' RESUMO DO VALOR ')

    print(f'A metade de {moeda(preço)} é \t{metade(preço, True)}')
    sleep(0.5)
    print(f'O dobro de {moeda(preço)} é \t\t{dobro(preço, True)}')
    sleep(0.5)
    print(f'Aumentando {a} temos \t\t{aumentar(preço, a, True)}')
    sleep(0.5)
    print(f'Diminuindo {b} 13% temos \t{diminuir(preço, b, True)}')
    sleep(0.5)
# ???????????????????????????????????????????
# AQUI QUERIA QUE O TEXTO FORMATADO DEVOLVESSE O VALOR DE COMP
# SÓ CONSEGUI FAZENDO DE COMP GLOBAL, VC CONHECE ALGO COMO RETURN
    print('-'*comp)
