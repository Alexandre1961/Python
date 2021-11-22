'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo,
da esquerda para a direita.
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
vertebrado:
    ave:
        carnivoro:
            aguia
        onivoro:
            pomba
    mamifero:
        onivoro:
            homem
        herbivoro:
            vaca

invertebrado:
    inseto:
        hematofogo:
            pulga
        herbivaro:
            lagarta
    anelideo:
        hematofago:
            sanguessuga
        onivoro:
            minhoca

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

vertebrado
mamifero
onivoro

homem

vertebrado
ave
carnivoro

aguia

invertebrado
anelideo
onivoro

minhoca'''

c1 = input()
c2 = input()
c3 = input()

if 'vertebrado' == c1:

    if c2 == 'ave':
        if c3 == 'carnivoro':
            print('aguia')
        if c3 =='onivoro':
            print('pomba')

    if c2 == 'mamifero':
        if c3 == 'onivoro':
            print('homem')
        if c3 == 'herbivoro':
            print('vaca')

if c1 == 'invertebrado':

    if c2 == 'inseto':
        if c3 == 'hematofago':
            print('pulga')
        if c3 == 'herbivoro':
            print('lagarta')

    if c2 == 'anelideo':
        if c3 == 'hematofago':
            print('sanguessuga')
        if c3 == 'onivoro':
            print('minhoca')
