#lendo arquivo e criando as listas
arquivo = open(r'D:\ACM Google Drive\Programação\Python\pythonexercicios\cesar_school\herois.txt')
print(arquivo)
marvel_lista = []
dc_lista = []
for linha in arquivo:
  linha_modificada = linha.lower().split()
  #print(linha_modificada)
  if 'dc' in linha_modificada:
      dc_lista.append(linha)
  elif 'marvel' in linha_modificada:
      marvel_lista.append(linha)

# escrevendo DC
DC = open(r'D:\ACM Google Drive\Programação\Python\pythonexercicios\cesar_school\DC.txt', 'w')
DC.close()
DC = open(r'D:\ACM Google Drive\Programação\Python\pythonexercicios\cesar_school\DC.txt', 'a')
for linha in dc_lista:
    DC.write(linha)
DC.close()
DC = open(r'D:\ACM Google Drive\Programação\Python\pythonexercicios\cesar_school\DC.txt')
for linha in DC:
    print(linha)

#escrevendo marvel
MARVEL = open(r'D:\ACM Google Drive\Programação\Python\pythonexercicios\cesar_school\MARVEL.txt', 'w')
MARVEL.close()
MARVEL = open(r'D:\ACM Google Drive\Programação\Python\pythonexercicios\cesar_school\MARVEL.txt', 'a')
for linha in marvel_lista:
    MARVEL.write(linha)
MARVEL.close()
MARVEL = open(r'D:\ACM Google Drive\Programação\Python\pythonexercicios\cesar_school\MARVEL.txt')
for linha in MARVEL:
    print(linha)


