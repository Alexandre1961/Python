n = int(input())

cem = int(n/100)
cem_r = n%100

cinq = int(cem_r/50)
cinq_r = cem_r%50

vinte = int(cinq_r/20)
vinte_r = cinq_r%20

dez = int(vinte_r/10)
dez_r = vinte_r%10

cinc = int(dez_r/5)
cinc_r = dez_r%5

dois = int(cinc_r/2)

dois_r = cinc_r%2
print(dois_r)

print ('{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'.format(n, cem, cinq, vinte, dez, cinc, dois, dois_r ))