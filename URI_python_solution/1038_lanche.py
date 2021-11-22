precos = [4 , 4.5 , 5 , 2 , 1.5]

x, y = input().split(' ')
x = int(x)
y = int(y)
preco = precos[x-1] * y

print(f'Total: R$ {preco:.2f}')