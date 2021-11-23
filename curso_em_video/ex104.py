'''Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaint(msg):
    n = input(msg)
    while n.isnumeric() == False:
        print('\033[0;31m ERRO, digite um numero inteiro válido\033[m')
        n = input(msg)
    n = int(n)
    return n

#programa principal
n = leiaint('Digite um numero: ')
print(f'Voce cabou de digitar o numero {n} ele é ', type(n))

