print(f'{" TRADANDO EXCESSÕES ":?^40}')
try:
    a = int(input('a = '))
    b = int(input('b = '))
    r = a / b
except: # irá mostrar a mensagem e não o erro
    print('infelizmente tivemos um problema (: ')
else:
    print(f'O resultado é {r:.2f}.')
finally:
    print('-'*20)
    print(' VOLTE SEMPRE '.center(20))
    print('-' * 20)


