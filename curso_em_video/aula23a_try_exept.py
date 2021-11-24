
try:
    a = int(input('a = '))
    b = int(input('b = '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um erro com tipo de dados')
except ZeroDivisionError:
    print(f'não é possivel dividir por zero')
except KeyboardInterrupt:
    print(f'O usuário não informou os dados')
except Exception as erro:
    print(f'Problema class =  {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally: # opcional
    print('-'*20)
    print(' VOLTE SEMPRE '.center(20))
    print('-' * 20)