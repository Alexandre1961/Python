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
