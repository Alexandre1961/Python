'''Neste desafio, você tem a tarefa de criar um script Python para
analisar os registros financeiros de sua empresa. Você fornecerá um conjunto de dados financeiros
chamado dados_financeiros.txt. O conjunto de dados é composto por duas colunas: Data e Lucros/Perdas, separados por virgula. (Felizmente, sua empresa tem padrões bastante flexíveis para a contabilidade, então os registros são simples.)
Sua tarefa é criar um script Python que analise os registros para calcular cada um das seguintes informações:
O número total de meses incluídos no conjunto de dados
O valor total líquido de "Lucros / Perdas" durante todo o período
A média dos "Lucros / Perdas" durante todo o período
A média das mudanças em "Lucros / Perdas" durante todo o período
O maior aumento nos lucros (data e valor) durante todo o período
A maior redução nas perdas (data e valor) ao longo de todo o período
Por exemplo, sua análise deve ser semelhante a esta abaixo:

Analise financeira
----------------------------
Total de meses: 86
Total: $ 38382578
Média: $ 446309,04
Variação da média: $ -2315,12
Maior aumento nos lucros: fevereiro de 2012 ($ 1926159)
Maior redução nos lucros: setembro de 2013 ($ -2196167)'''

# Primeiro vamo atribuir nossos dados em uma variável (tabela)
with open('dados_financeiro.txt') as dados:
    tabela = [linha.replace('\n', '') for linha in dados]
    # Agora vamos criar três listas para armazenar as datas e os lucros/perdas
    datas = []
    lucros_perdas = []
    mudancas = []
    # Percorremos a tabela partindo da linha de numero 2
    for i, info in enumerate(tabela, 1): # ou enumerate(tabela[1:])
        data, lucro_perda = info.split(',')
        datas.append(data)
        lucro_perda = int(lucro_perda)
        lucros_perdas.append(lucro_perda)
        mudanca = lucro_perda - lucros_perdas[i - 1]
        mudancas.append(mudanca) if i > 0 else None

    total_meses = len(datas)
    valor_liquido = sum(lucros_perdas)
    media = valor_liquido / len(lucros_perdas)
    media_mudanca = sum(mudancas) / len(mudancas)
    maior_aumento = max(mudancas)
    maior_perda = min(mudancas)
    melhor_mes = datas[mudancas.index(maior_aumento) + 1]
    pior_mes = datas[mudancas.index(maior_perda) + 1]

with open('analise.txt', 'w') as analise:
    analise.write(
        f'Analise Financeira\n{"-" * 20}\nTotal de Meses: {total_meses}\nTotal: $ {valor_liquido:.2f}\nMédia: $ {media:.2f}\nVariação da média: $ {media_mudanca:.2f}\nMaior aumento nos lucros: {melhor_mes} $ {maior_aumento}\nMaior redução nos lucros: {pior_mes} $ {maior_perda}')

