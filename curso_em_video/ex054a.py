from datetime import date
velho=0
novo=0
for c in range(1,7,1):
    a=int(input('Data de nascimento da {}º pessoa'.format(c)))
    idade=(date.today().year)-a
    if idade>=18:
        velho+=1
    else:
        novo+=1
print('O número de pessoas maiores de idade é: {}'.format(velho))
print('O número de pessoas menores de idade é: {}'.format(novo))