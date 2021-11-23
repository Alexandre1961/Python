'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Qual a média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif 7 > aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
elif aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
print(f"{' INFORMAÇÂO ':*^35}")
print(f"Nome: {aluno['nome']}")
print(f"Média de {aluno['nome']} = {aluno['média']}")
print(f"A situação de {aluno['nome']} é {aluno['situação']}")
print(f"{' FIM ':*^35}")


