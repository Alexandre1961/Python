''' Crie um programa que declare uma matriz de dimensão 3x3
 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.
'''
# ESTUDE A NECESSIDADE OBRIGATORIA DE PASSAGEM DE DADOS PARA LISTAS COMPOSTAS
matriz = [[], [], []]
lin = 0
while lin < 3:
    c = 0
    for c in range(0, 3):
        matriz[lin].append(int(input(f'Digite uma valor para {[lin]} {[c]} : ')))
    lin += 1
print('-='*20)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'{" FIM ":*^30}')
