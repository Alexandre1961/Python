''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
resp = 'S'
while resp == 'S':
    lista.append(int(input('Digite numero: ')))
    resp = str(input('Continua S/N ')).strip().upper()
    while resp not in "SN":
        resp = str(input('Continua S/N ')).strip().upper()
    if resp == 'N':
        break

print(f'Foram digitados {len(lista)} numeros')
#sort não funciona nesta instancia
#print(f'A lista digitada decrescente é : {lista.sort(reverse=True)}')
lista.sort(reverse=True)
print(f'A lista digitada decrescente é : {lista}')
if 5 in lista[0:]:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não foi digitado')





