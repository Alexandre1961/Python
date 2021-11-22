x = input().split(' ')

a = int(x[0])
b = int(x[1])
c = int(x[2])

resultado = (a+b+abs(a-b))/2
eh_maior = int((resultado+c+abs(resultado-c))/2)

print(f'{eh_maior} eh o maior')