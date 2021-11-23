'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

count = 0
lista = (int(input('Digite um numero:')),
         int(input('Digite um numero:')),
         int(input('Digite um numero:')),
         int(input('Digite um numero:')))
print(lista)
print('=-'*20)
if 9 in lista:
    print(f'O numero nove apareceu {lista.count(9)} vezes')
else:
    print('O numero 9 não foi digitado')
print('=-' * 20)
if 3 in lista:
    print(f'A primeira vez que apareceu o numero 3 foi na posição {lista.index(3)}ª')
else:
    print('O numero 3 não foi digitado')
print('=-' * 20)
print('Os numeros pares da lista são: ')
for n in lista:
    if n % 2 == 0:
        print(f'{n}', end=', ')
        count += 1
if count == 0:
    print('Não foram digitados numeros pares na lista')
print('=-'*20)
print(f'{" FIM ":&^20}')





