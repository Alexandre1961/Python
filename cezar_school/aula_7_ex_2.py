'''2. Faça um programa que crie uma pasta no diretorio atual do notebook e crie dentro dele um arquivo chamado,
lista_de_chamada.txt, na qual devera ter 5 nomes informados pelo usuario.'''

import os
dir = "chamada"
if not os.path.exists(dir):
  os.mkdir(dir)
arquivo = open(dir +'\lista_de_chamada', 'w')
arquivo.close()

arquivo = open(dir +'\lista_de_chamada', 'a')
for i in range(0,5):
  arquivo.write(input('Digite o nome do aluno: ')+'\n')
arquivo.close()

arquivo = open(dir +'\lista_de_chamada')
for linha in arquivo:
  print(linha)