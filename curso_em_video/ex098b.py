from time import sleep


def contador(a, b, c):
    d = a
    if a > b:
        c = c*-1
    while True:
        if d != b:
            print(d, end=' / ')
            d += c
            sleep(0.5)
            continue
        print(d, end=' ')
        break
    print('FIM')