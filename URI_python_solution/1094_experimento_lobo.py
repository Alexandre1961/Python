# EU FIZ ESSA USANDO DICIONÁRIO, FABRICIO NÃO ENSINOU ISSO, MAS FACILITA MUITO A VIDA

n = int(input()) # numero de testes

# cada caso tem uma quantidade de animais (qnt_animais) e qual animal foi usado (C, R ou S):

dados = {'C':0 , 'R':0 , 'S':0}

for i in range(n):
  qnt_animais, animal = input().split(' ')
  qnt_animais = int(qnt_animais)
  dados[animal] += qnt_animais

total_animais = sum(dados.values())
total_coelhos = dados['C']
total_ratos = dados['R']
total_sapos = dados['S']

perc_coelhos = (total_coelhos/total_animais)*100
perc_ratos = (total_ratos/total_animais)*100
perc_sapos = (total_sapos/total_animais)*100

resultado = f'''Total: {total_animais} cobaias
Total de coelhos: {total_coelhos}
Total de ratos: {total_ratos}
Total de sapos: {total_sapos}
Percentual de coelhos: {perc_coelhos:.2f} %
Percentual de ratos: {perc_ratos:.2f} %
Percentual de sapos: {perc_sapos:.2f} %'''

print(resultado)