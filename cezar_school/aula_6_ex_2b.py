'''cesar aula 6 ex 2
Crie um programa que registra as notas de uma pessoa na escola (como o boletim) em um arquivo.
Em seguida, leia todos os valores para imprimir o menor valor, o maior e a média.
Dica: Se você usar listas, pode usar as funções min() e max().'''

#função max min media
def min_max_media(lista, txt):
    maior = 0
    menor = 0
    soma = 0
    media = 0
    if txt == '+':
        maior = max(lista)
        return float(maior)
    elif txt == '-':
        menor = min(lista)
        return float(menor)
    elif txt == 'm':
        for linha in lista_notas:
            soma += float(linha)
        media = soma/len(lista_notas)
        return media

#cria boletim.txt
arquivo = open('boletim.txt','w')
arquivo.close()
arquivo = open('boletim.txt', 'a')

#carrega aruivo boletim.txt
flag = True
while flag == True:
  nota = float(input('Digite a nota do aluno: '))
  arquivo.write(str(nota)+'\n')
  resposta = input('Deseja continuar s/n: ')
  if resposta in 'nN':
    flag = False
arquivo.close()

#cria lista de notas
lista_notas = []
arquivo = open('boletim.txt')
for linha in arquivo:
    lista_notas.append(linha)
arquivo.close()

# chama função

maior = min_max_media(lista_notas,'+')
menor = min_max_media(lista_notas,'-')
media = min_max_media(lista_notas,'m')

#mostra o resultado
print(f' A maior nota é {maior:.2f}, a menor é {menor:.2f} e a media é {media:.2f}')