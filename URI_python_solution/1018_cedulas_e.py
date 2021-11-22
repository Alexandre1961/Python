valor = int(input())

nota100 = int(valor/100)
resto100 = valor%100

nota50 = int(resto100/50)
resto50 = resto100%50

nota20 = int(resto50/20)
resto20 = resto50%20

nota10 = int(resto20/10)
resto10 = resto20%10

nota5 = int(resto10/5)
resto5 = resto10%5

nota2 = int(resto5/2)
resto2 = int(resto5%2)

print(f'''{valor}
{nota100} nota(s) de R$ 100,00
{nota50} nota(s) de R$ 50,00
{nota20} nota(s) de R$ 20,00
{nota10} nota(s) de R$ 10,00
{nota5} nota(s) de R$ 5,00
{nota2} nota(s) de R$ 2,00
{resto2} nota(s) de R$ 1,00''')