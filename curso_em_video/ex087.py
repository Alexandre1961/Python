''' Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somatc = mvl2 = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somatc += matriz[l][c]
mvl2 = max(matriz[1])
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos numeros pares é {somapar}')
print(f'A o soma dos valores da terceira coluna é {somatc}')
print(f'O maior valor da linha 2 é {mvl2}')
print(f'{" FIM ":&^60}')
