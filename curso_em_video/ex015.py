# ex015
d = int(input('Quantos dias de uso: '))
vd = float(input('Valor de aluguel por dia: '))
k = float(input('Quantos kilometros rodados: '))
vk = float(input('Valor do km: '))
print('Para {}dias e {}km o valor de aluguel do carro é de R${:2f}'.format(d, k, (d * vd) + (k * vk)))
