'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
- A média da turma
– A situação (opcional)'''
def notas(* lst, sit=False):
    dados = {}
    dados['maior'] = max(lst)
    dados['menor'] = min(lst)
    dados['media'] = sum(lst) / len(lst)
    situação = ''
    if sit:
        if dados['media'] >= 7:
            dados[situação] = 'BOA'
        elif 5 <= dados['media']: # não precisa < 7 pois esta condição foi verificada linha acima
            dados['situação'] = 'RAZOAVÈL'
        else: # não precisa  dados['media'] < 5 pois as outras condições foram verificadas linhas acima
            dados['situação'] = 'RUIM'
    return dados


#programa principal
resp = notas(5, 3 , 3, 3, sit=True)
print('resp = ', resp)
