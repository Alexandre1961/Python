# dada uma distancia de viagem
# calcule o valor da passagem
# sabendo que até 200km o km vale R$0.50 acima R$0.45
dis = int(input("Qual a distancia da viagem em km? "))
if dis <= 200:
    print('Para uma viagem de {}Km o valor da passagen é R${:.2f}'.format(dis, (dis * 0.5)))
else:
    print('Para uma viagem de {}km o valor da passagem é R${:.2f}'.format(dis,(dis * 0.45)))
print('{:+^20}'.format('BOA VIAGEM'))

if dis <= 200:
    preco = dis * 0.5
else:
    preco = dis * 0.45
print('O preço da passagem é de R${:.2f}'.format(preco))
# if line, operador ternário,  if simplificado
preco = dis * 0.5 if dis <= 200 else dis * 0.45
print('O preço é R${:.2f}'.format(preco))
