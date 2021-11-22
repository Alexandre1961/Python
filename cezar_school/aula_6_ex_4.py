'''A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
e identificar os usuários com maior espaço ocupado.
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

Neste arquivo, o nome do usuário possui 15 caracteres.
A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

 ACME Inc.       Uso do espaço em disco pelos usuários

 Nr.  Usuário        Espaço utilizado     % do uso

 1    alexandre       434,99 MB             16,85%
 2    anderson       1187,99 MB             46,02%
 3    antonio         117,73 MB              4,56%
 4    carlos           87,03 MB              3,37%
 5    cesar             0,94 MB              0,04%
 6    rosemary        752,88 MB             29,16%

 Espaço total ocupado: 2581,57 MB
 Espaço médio ocupado: 430,26 MB
'''
arquivo_r = open('relatorio.txt', 'w')
arquivo_r.write('ACME Inc.       Uso do espaço em disco pelos usuários\n\n')
arquivo_r.write(f'{"NR.":<5}{"Usuario":<18}{"Espaço utilizado":<20}{"% de uso":<10}\n\n')
arquivo_r.close()

tamanho = []
usuario = []

#cria as listas
arquivo = open('usuarios.txt')
for linha in arquivo:
    nova_linha = linha.replace('\n',' ')
    usuario.append(nova_linha[0:15])
    tamanho.append(int(nova_linha[16:])/1048576)
arquivo.close()

#acha valores
total = sum(tamanho)
media = total / len(tamanho)

#escreave relatorio
arquivo_r = open('relatorio.txt', 'a')
for i in range(0,len(tamanho)):
    arquivo_r.write(f'{i+1:<5}{usuario[i]:<11}{tamanho[i]:>17.2f} MB {tamanho[i]/total*100:>10.2f}%\n')
arquivo_r.write(f'\nEspaço total ocupado: {total:.2f} MB\n')
arquivo_r.write(f'Espaço medio ocupado: {media:.2f} MB\n')












