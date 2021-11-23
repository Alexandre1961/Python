'''
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''
qt = 0
soma = 0
while True:
    num = int(input('Digite um numero inteiro (999 para sair): '))
    if num == 999:
        break
    qt += 1
    soma += num
print(f'voce digitou {qt} numeros e a soma deles é {soma}')



