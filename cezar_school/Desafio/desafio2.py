'''PyVotação
Neste desafio, você tem a tarefa de ajudar uma pequena cidade rural a modernizar seu processo de contagem de votos. (Até agora, o tio Cleiton vinha contando-os um por um com confiança, mas, infelizmente, sua concentração não é o que costumava ser.)

Você receberá um conjunto de dados de enquete chamado dados_eleção.txt. O conjunto de dados é composto por três colunas: ID do eleitor,Município e Candidato. Sua tarefa é criar um script Python que analise os votos e calcule cada uma das seguintes informações:

O número total de votos expressos

Uma lista completa de candidatos que receberam votos

A porcentagem de votos que cada candidato ganhou

O número total de votos que cada candidato ganhou

O vencedor da eleição com base no voto popular.

Por exemplo, sua análise deve ser semelhante a esta abaixo:

Resultados eleitorais
-------------------------
Total de votos: 3521001
-------------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
-------------------------
Vencedor: Khan
-------------------------
Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto resultado.txt com os resultados.'''

with open('dados_elecao.txt') as dados:
    eleicao = [linha.replace('\n', '') for linha in dados]
    ids = []
    municipios = []
    candidatos = []
    lista_candidatos = []
    votos = []
    porc_votos = []

    for linha in eleicao[1:]:
        id_eleitor, municipio, candidato = linha.split(',')
        ids.append(id_eleitor)
        print(ids)
        municipios.append(municipio)
        candidatos.append(candidato)
        lista_candidatos.append(candidato) if candidato not in lista_candidatos else None

    # Contar votos e percentual de votos
    for i, cand in enumerate(lista_candidatos):
        votos.append(candidatos.count(cand))
        porc_votos.append(votos[i] / len(candidatos))

    total_votos = sum(votos)

    vencedor = lista_candidatos[votos.index(max(votos))]

    resultado = ''
    for i, nome in enumerate(lista_candidatos):
        resultado += f'{nome}: {porc_votos[i]:.1%} ({votos[i]})\n'

    resultado_final = f'''
  Resultados eleitorais
-------------------------
Total de votos: {total_votos}
-------------------------
{resultado}
-------------------------
Vencedor: {vencedor}
-------------------------
  '''

    with open('resultado.txt', 'w') as resultado:
        resultado.write(resultado_final)
