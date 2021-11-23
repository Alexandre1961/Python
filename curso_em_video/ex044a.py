'''
calcule o valor  a ser pago de um produto de acordo com a sua condição de pagamento:
a vista no R$ = 10% de desconto
a vista no débito = 5% de desconto
até 2 vezes no cartão = preço normal
3 vezes ou mais = 20%/mes de juros
'''
preço = float(input('Qual o preço do produto: '))
parcela = int(input('''Em quantas vezes que pagar
0 para á vista em dinheiro
1 para a vista no cartão
ou qual numero de  parcelar): '''))
if parcela == 0:
    print('A vista em dinheiro  voce pagara R${:.2f}.'.format(preço * 0.9))
elif parcela == 1:
    print('A vista no cartão voce pagará R${:.2f}.'.format(preço * 0.95))
elif parcela == 2:
    print('Em {}X voce pagará R${:.2f}/mes, total de {:.2f} . '.format(parcela, preço / 2, preço ))
elif parcela >= 3:
    print('Em {}X voce pagara R${:.2f}/mes, total de {:.2f}.'.format(parcela, (preço + (preço * 0.2 * parcela))/parcela, preço + (preço * 0.2 * parcela)))
print('{:&^30}'.format(' FIM '))
