'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

nomes = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'trese', 'quatorze', 'quinze', 'dezeseis',
         'dezesete', 'dezoito', 'dezenove','vinte')

while True:
    numero = int(input('Digite um numero: '))
    if 0 <= numero <= 20:
        print(f'Voce digitou o numero {nomes[numero]}')
    else:
        numero = int(input('de 0 a 20 burro: '))
    resp = str(input('Sair S/N > ')).strip().upper()
    if resp not in 'SN':
        resp = str(input('Sair S/N > ')).strip().upper()
    if resp == 'S':
        break
print(f'{" FIM ":&^30}')