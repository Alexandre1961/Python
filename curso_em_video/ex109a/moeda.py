def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa / 100)
    return moeda(res)


def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa / 100)
    return moeda(res)


def dobro(preço=0):
    res = preço * 2
    return moeda(res)

def metade(preço=0):
    res = preço / 2
    return moeda(res)

def moeda(preço, moeda = 'R$'):
    return f'{moeda}{preço:>7.2f}'.replace('.', ',')
