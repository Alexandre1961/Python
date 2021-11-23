'''
calcule o valor  a ser pago de um produto de acordo com a sua condição de pagamento:
a vista no R$ = 10% de desconto
a vista no débito = 5% de desconto
até 2 vezes no cartão = preço normal
3 vezes ou mais = 20%/mes de juros
'''
preço = float(input('Qual o preço do produto: '))
c = int(input('''Qual a condição de pagamento
[1] a vista
[2] a vista no bébito
[3] até duas vezes
[4] 3 vezes ou mais
Qual sua opção: '''))
if c == 1:
    print('O preço a vista com 10% de desconto é R${}.'.format(preço*0.9))
elif c == 2:
    print('O preço a vista no cartão é R${:.2f}'.format(preço*0.95))
elif c == 3:
    print('O preço de R${:.2f} em 2X é R${:.2f} mensal'.format(preço, preço / 2))
elif c == 4:
    p = int(input('Quantas parcelas: '))
    j = preço * 0.2 * p
    if p < 3:
        print('Esta opção não permite este numero de parcelas')
    else:
        print('Voce pagara R${} de juros em {} meses'.format(j, p))
        print('O preço final é de R${:.2f} em {} vezes voce pagara R${:.2f} mensal'.format(preço+j, p, (preço + j) / p))
else:
    print('Condição invalida tente novamente')
print('{:&^30}'.format(' FIM '))

