'''
tupla = (2, 4, 7, 9)
tupla[3] = 4
Traceback (most recent call last):
  File "D:\ACM Google Drive\Programação\Python\python_aulas\aula17a.py", line 2, in <module>
    tupla[3] = 4
TypeError: 'tuple' object does not support item assignment
'''
lista = [2, 4, 7, 9]
print('A lista é : ', lista)
# lista[4] = 5 #erro não existe posição 4
'''    lista[4] = 5 #erro
IndexError: list assignment index out of range'''
lista[3] = 5 # vai substituir a posição 3 com o numero 5
print('lista[3] = 5 ', lista, ' substituiu a posição 3 com o numero 5')
lista.append(11) # adiciona 11 no final da lista
print('lista.append(11) =', lista, ' adiciona 11 no final da lista')
lista.insert(2, 33) # insere na posisção 2 o numero 33
print('lista.insert(2, 33) = ', lista, 'insere na posisção 2 o numero 33')
lista.sort()
print('lista.sort() = ', lista)
lista.sort(reverse=True)
print('lista.sort(reverse=True) = ', lista)

print(f'Esta lista tem {len(lista)} elementos')

lista.pop()
print('lista.pop =', lista, 'remove ultimo elemento')
lista.pop(2)
print('lista.pop(2) =', lista, 'remove elemento 2')
lista.insert(2, 4)
print('lista.insert(2, 4) = ', lista, 'insere na posição 2 o numero 4')
lista.remove(4)
print('lista.remove(4) = ', lista, 'remove o primeiro 4 que encontra')
if 13 in lista:
    lista.remove(13)
else:
    print('Numero 13 não esta na lista')
