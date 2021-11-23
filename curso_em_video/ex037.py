'''
programa pede um numero inteiro
o usuário escolhe uma base de conversão:
1 binario
2 octal
3 hexadecimal
'''
num = int(input('Digite um numero inteiro: '))
pos = int(input('''Escolha a conversão: 
[1] para biário
[2] para octal
[3] para hexadecimal 
Sua escola :'''))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
if pos == 1:
    print('A conversão do inteiro {} para binário é {} '.format(num, binario))
elif pos == 2:
    print('A conversão do inteiro {} para octal é {}'.format(num, octal))
elif pos == 3:
    print('A conversão do inteiro {} para hexadecimal é {}'.format(num, hexadecimal))

if pos == 1:
    print('A conversão do inteiro {} para binário é {} '.format(num, bin(num)[2:]))
elif pos == 2:
    print('A conversão do inteiro {} para octal é {}'.format(num, oct(num)[:2]))
elif pos == 3:
    print('A conversão do inteiro {} para hexadecimal é {}'.format(num, hex()[2:]))

print('Opção invalida tente novamente!')
print('{:#^30}'.format(' FIM '))