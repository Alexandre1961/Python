'''Def funções'''
def titulo(texto):
    print('-='*15)
    print(f'{texto:&^30}')
    print('-='*15)
# 2 linhas

def tituloFormatado(texto):
    comp = len(texto)+10
    print('*'*comp)
    print(texto.center(comp))
    print('*' * comp)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

def contador(* num):
    print(f'A quantidade de numeros passados são {len(num)}')
    for valores in num:
        print(f'{valores}', end=' ')
    print()

def dobra(lis):
    print('Antes de dobra(lis), lista = ', lis)
    for c in range(0, len(lis)):
        lis[c] *= 2
    print('Após dobra(lis), lista = ', lis)
    ''' outro exemplo
    pos = 0
    while pos < len(lis):
    lis[pos] *= 2
    pos += 1
    '''
def somaLista(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os {valores} temos {s}')


titulo(' def - FUNÇÕES ')
##########################################
msg = (' Função de texto para print ').upper()
titulo(msg)
msg = (' Função de texto formatado para upper e center() de acordo com seu tamanho ').upper()
##########################################
tituloFormatado(msg)
print('Usando def de soma a + b >> soma(a, b)')
soma(4, 5)
print('Usando valores explicitos fora da ordem como soma(b = 4 , a = 8)')
soma(b=4, a=8)
tituloFormatado('Empacotamento e Desempacotando de valores')
contador(1, 2, 3, 4, 5)
contador(4, 8, 6)
tituloFormatado(' Passando listas para funções ')
print('Listas são variavéis compostas, não precisam de empacotamento')
lista = [7, 2, 5, 0, 2]
dobra(lista)
dobra([9, 4, 1])



