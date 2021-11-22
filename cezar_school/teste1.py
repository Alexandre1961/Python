resultado = []
for i in range(int(input())):
  string = input()
  desloc_direita = []

  for caracter in string:
    if caracter.isalpha():
      desloc_direita.append(chr(ord(caracter) + 3))
    else:
      desloc_direita.append(caracter)

  inverter = desloc_direita[::-1]


  desloc_esquerda = [chr(ord(car) - 1) for car in inverter[int(len(inverter)/2)+1:]]


  resultado.append(''.join(inverter[:int(len(inverter)/2)+1] + desloc_esquerda[:int(len(inverter)/2)]))


for i in resultado:
  print(i)
