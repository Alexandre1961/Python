'''Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.264.5
192.168.0.256
O arquivo de saída possui o seguinte formato:

      [Endereços válidos:]
      200.135.80.9
      192.168.1.1
      8.35.67.74
      1.2.3.4

      [Endereços inválidos:]
      257.32.4.5
      85.345.1.2
      9.8.264.5
      192.168.0.256
'''
def valida_ip(texto):
  valores = texto.replace("\n","").split('.')
  for numero in valores:
    # desafio ip com letra
    #if numero.isdigit() and int(numero) > 255:
    if int(numero) > 255 or int(numero) < 0:
      return False
  return True

ips = []
with open('ips.txt') as arquivo:
  for linha in arquivo:
    ips.append(linha)


ips_validos = []
ips_invalidos = []

for valores in ips:
  if valida_ip(valores):
    ips_validos.append(valores)
  else:
    ips_invalidos.append(valores)

#[Endereços válidos:]
#200.135.80.9
#192.168.1.1
#8.35.67.74
#1.2.3.4

#[Endereços inválidos:]
#257.32.4.5
#85.345.1.2
#9.8.264.5
#192.168.0.256

with open('arquivo_final_ip.txt','w') as arquivo:
  arquivo.write("[Endereços válidos:]")
  for valores in ips_validos:
    arquivo.write(valores)

  arquivo.write("[Endereços inválidos:]")
  for valores in ips_invalidos:
    arquivo.write(valores)



