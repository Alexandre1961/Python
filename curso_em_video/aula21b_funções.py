def textoFormatado(txt):
    comp = len(txt) + 10
    txt = txt.upper()
    print('?' * comp)
    print(txt.center(comp).upper())
    print('?' * comp)


def texto(txt):
    print(txt*30)


def var(b):
    # global a assume a variavle global a dentro de def
    a = 8  # variavél local
    b += 4  # variavél local
    c = 2  # variavél local
    print(f'A dentro vale {a}')
    print(f'b += 4 dentro vale {b}')
    print(f'C dentro vale {c}')


def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'Dentro de def soma(a,b,c) s = {s}')
    return s # irá retornar o valor da soma para a chamada da função


def fatorial(num=1): # 1 se nehum valor for informado
    f = 1 #pega o c inicial e assume o valor
    for c in range(num, 1, -1):
        f *= c #inicio f = 1 e c = 5, f=5 c= 4, f=120 c= 3, ....
    return f

def par(num):
    if num % 2 == 0:
        num = True
    else:
        num = False
    return num



textoFormatado('Variavel global e local')
a = 9
print(f'Declarande a=9 no programa principal a = {a}')
print('Chamando def var(b) onde b será a variavel a')
var(a)
textoFormatado(' retorno de valores - return ')
print('Declarando que retornoDef = soma(4,7,2)')
retornoDef = soma(4,7,2)
print(f'retornoDef = {retornoDef}')
print('Usando o print para o return temos > ',soma(3, 7, 8))
r1 = soma(1,3,5)
r2 = soma(2,4)
r3 = (7)
print('''Passando para soma \nr1 = soma(1,3,5)
r2 = soma(2,4)
r3 = (7)''')
print(f'Os valores de retorno serão\nr1 = {r1}, r2 = {r2}, r3 = {r3}')
texto('-')
f1 = fatorial(5)
f2 = fatorial(6)
f3 = fatorial()
print(f' f1 = {f1}, f2 = {f2},f3 = {f3}')
texto('-')
x = int(input('Digite um numero: '))
print(par(x))
print('Logo na condição if True ou False')
if par(x):
    print('É par')
else:
    print('É impar')

