valores = []
#valores = lista()
valores.append(5)
valores.append(4)
valores.append(9)
for v in range(0, 3):
    v = int(input('Digite um valor: '))
    valores.append(v)
for v in valores:
    print(v)
for p, v in enumerate(valores):
    print(f' o valor {v} esta na posição {p}')