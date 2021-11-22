'''cesar aula 6 ex 2
Crie um programa que registra as notas de uma pessoa na escola (como o boletim) em um arquivo.
Em seguida, leia todos os valores para imprimir o menor valor, o maior e a média.
Dica: Se você usar listas, pode usar as funções min() e max().'''
arquivo = open('boletim','w')
arquivo.close()
arquivo = open('boletim', 'a')
flag = True
conta = 0
maior = 0
menor = 0
soma = 0
while flag == True:
  nota = float(input('Digite a nota do aluno: '))
  if conta == 0:
    menor = maior = nota
  soma = soma + nota
  arquivo.write(str(nota))
  conta += 1
  resposta = input('Deseja continuar s/n: ')
  if resposta in 'nN':
    flag = False
  if nota > maior:
    maior = nota
  elif nota < menor:
    menor = nota
arquivo.close()
print(f' A maior nota é {maior:.2f}, a menor é {menor:.2f} e a media é {soma/conta:.2f}')
