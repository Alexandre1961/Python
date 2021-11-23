#digite uma velocidade de carro
# se ultrapassar 80km mande mensagem "voce foi multado"
# calcule o valor sabendo que cada km excedente vale R$7.00
ve = int(input('Digite a velocidade do carro: '))
print(ve)
if ve > 80:
    mu = (ve - 80) * 7.00
    print('Sua velocidade registrada foi de {}, voce foi multado em no valor de R${:.2f}'.format(ve, mu))
    print('Dirija com mais prudencia')
print('boa viagem')
