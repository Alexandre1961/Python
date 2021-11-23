'''Melhore o DESAFIO 61,
perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
primeiro = int(input('Qual o primeiro termo da PA: '))
razão = int(input('Qual a fazão da PA: '))
numero_termos = int(input('Quantos termos da PA quer mostrar: '))
cont = 1
mais = numero_termos
while mais != 0:
    while cont <= numero_termos:
        print(primeiro, end='')
        primeiro += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais quer mostrar: '))
    if mais != 0:
        numero_termos += mais
print('FIM')

