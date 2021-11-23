'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
nomes = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'trese', 'quatorze', 'quinze', 'dezeseis',
         'dezesete', 'dezoito', 'dezenove','vinte')
print('=-'*30)
numero = int(input('Digite um numero entre 0 e 20: '))

while numero < 0 or numero > 20:
    numero = int(input('Tem que ser entre 0 e 20: '))
print(f'Voce digitou o numero {nomes[numero]}')
print('=-'*30)
