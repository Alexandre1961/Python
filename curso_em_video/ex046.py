#contagem regressiva de 10 até 0 com pausa de 1 segundo entre eles
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("fim")