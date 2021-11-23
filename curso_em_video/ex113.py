def leiaInt(msg): # recebe mensagem do programa principal
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m"ERRO" digite um numero inteiro\033[m')
        except KeyboardInterrupt:
            print('Valor não informado:')
            return 0
        else:break
    return n


def leiaFloat(msg): # recebe mensagem do programa principal
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m"ERRO" digite um numero inteiro\033[m')
        except KeyboardInterrupt:
            print('Valor não informado:')
            return 0
        else:
            break
    return n


# programa principal
num1 = leiaInt('Digite um numero inteiro: ') # vai passar esta mensagem para leiaInt
num2 = leiaFloat('Digite um numero real: ') # vai passar esta mensagem para leiaInt
print(f'O numero inteiro é {num1} o numero real é {num2}')