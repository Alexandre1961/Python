'''
programa de aprovação de emprestimo bancário
pergunta o valor da casa
o salario do comprador
quantos anos ele ira pagar
com juros 0%
o valor da parcela não pode exceder 30% do salário
se sim emprestimo negado
'''
valorimovel = float(input('Qual o valor dao imovél? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos para pagar? '))
valormensal = valorimovel / (anos * 12)
print('Valor mensal é R${:.2f}'.format(valormensal), end=' & ')
cond = 0.3 * salario
print('30% do salario é R${:.2f}'.format(cond))
if cond >= valormensal:
   print('Meus parabéns voce adquiriu um imovel de R${:.2f} pagando R${:.2f}/mes durante {}anos'.format(valorimovel, valormensal, anos))
else:
    print('Sentimos  muito mas a prestação de R${:.2f} exece 30% de seu salário de R${:.2f}, o emprestimo foi negado'.format(valormensal, salario))
print('Tenha um bom dia')
