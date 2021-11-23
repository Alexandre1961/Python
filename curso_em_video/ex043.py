'''
desenvolva lógica que leia o peso e altura de uma pessoa
calcule seu indice de massa corporea
e o classifique como:
abaixo de 18.5 = abaixo do peso
entre 18.5 e 25 = ideal
de 25 até 30 = sobrepeso
de 30 a 40 = obesidade
acima de 40 = obesidade morbida
IMC = peso(kg) / altura^2(metro)
'''
p = float(input('Qual é o seu peso (kg): '))
h = float(input('Qual é sua altura (m): '))
imc = p/(h**2)
print('IMC = {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso')
elif imc < 25:
    print('Voce esta no peso ideal')
elif imc < 30:
    print('Voce esta no sobrepeso')
elif imc < 40:
    print('Voce esta obeso')
elif imc > 40:
    print('Voce tem obesidade morbida')

print('{:&^30}'.format(' FIM '))

