# digite uma frase
# diga quantos 'a' ela tem
# que posição a primeira vez
# que posição aparece a ultima vez
frase = str(input('Digite uma frase: ')).strip().upper()
#frase = 'Eu estudo Python com o professor Guanabara'
print('__________1_________2_________3_________4_'   )
print('012345678901234567890123456789012345678901')
print(frase)
print('A frase tem {} letras "A" '.format(frase.count('A')))
print('O comprimento da frase é de {} caracteres '.format(len(frase)))
print('A letra "A" ocorre pela primeira vez na posição {}'.format(frase.find('A')))
print('A letra "A" ocorre pela ultima vez na posição {}'.format(frase.rfind('A')))




