'''
 Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.
'''
pesomaior = 0
pesomenor = 1000
for i in range(1, 6):
    peso = float(input('O peso da {}ª pessoas é: '.format(i)))
    if i == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso é {:.2f} e o menor é {:.2f} '.format(pesomaior, pesomenor))
