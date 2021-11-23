'''
desenvola um programa que leia:
o primeiro termo
e a razão
de uma PA.
No final mostre os 10 primeiros termos desta PA
'''
primeiro = int(input('Primeiro:'))
razão = int(input('Razão: '))
decimo = primeiro + (10-1) * razão
for i in range(primeiro, decimo +1, razão):
    print(i, end='-')
print('FIM')

