valor = int(input())
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0
resto = 0 # se não definir dá run time error var not defined


nota100 = int(valor/100)
resto = valor % 100

nota50 = int(resto/50)
resto = resto % 50

nota20 = int(resto/20)
resto = resto % 20

nota10 = int(resto/10)
resto = resto % 10

nota5 = int(resto/5)
resto = resto % 5

nota2 = int(resto/2)
resto = resto % 2

nota1 = resto

print('{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'.format(valor, nota100, nota50, nota20, nota10, nota5, nota2, nota1))