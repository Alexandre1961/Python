def cabeçalho():
    print('-'*30)
    print(f'{"MENU PRINCIPAL": ^30}')
    print('-' * 30)


def menu(msg):
    cabeçalho()
    print('''1 - Ver cadastro
2 - Cadasrar nova pessoas
3 - ALterar cadastro
4 - Excluir cadastro
5 - Sair do Sistema (esc)''')
    print('-' * 30)
    while True:
        try:
            op = int(input(msg))
        except (ValueError, TypeError):
            print(('Erro Digite um numero inteiro'))
        else:
            if str(op) not in '12345':
                print(f'{op} não é um item do menu')
            else:
                return int(op)


