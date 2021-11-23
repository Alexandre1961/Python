'''Dentro do pacote utilidadesCeV que criamos no desafio 112,
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            entrada  = print(f'ERRO, \033[0;31m\"{entrada}\" \033[mé um preço invalido')
        else:
            valido = True
    return float(entrada)
