'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
- A média da turma
– A situação (opcional)'''


def notas(* lst, sit=False):
    dados = {}
    situação = ''
    maior = menor = soma = media = 0
    dados['total'] = len(lst)
    for k, v in enumerate(lst):
        soma += lst[k]
        if k == 0:
            maior = menor = lst[0]
        else:
            if lst[k] > maior:
               maior = lst[k]
            if lst[k] < menor:
                menor = lst[k]
    media = soma / dados['total']
    dados['maior'] = maior
    dados['menor'] = menor
    dados['media'] = media
    if sit == True:
        if media >= 7:
            dados[situação] = 'BOA'
        elif 5 <= media <7:
            dados['situação'] = 'RAZOAVÈL'
        elif media < 5:
            dados['situação'] = 'RUIM'
    return dados


#programa principal
resp = notas(5, 5 , 3, 3, sit=True)
print('resp = ', resp)
