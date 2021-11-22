lista = []

lista = input('Digite algo: ')
print(lista)

numero = int(input('digite um numero: '))


#recursividade

def fatorial(n):
    fat = 1 if n == 0 else n * fatorial(n - 1)
    return fat

print(fatorial(numero))

