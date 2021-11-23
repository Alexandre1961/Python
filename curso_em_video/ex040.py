'''
leia 2 notas do alunos
calcule a média e avise-o
media abaixo de 5 reprovado
media entre 5 e 6.9 recuperação
média acima de 7 aprovado
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = round((n1 + n2)/2, 2)#trunc não funciona
print(media)
print(' A media entre as nota {:.1f} e {:.1f} é de {:.1f}.'.format(n1, n2, media))
if media >= 7.0:
    print('Sua média foi de {:.1f}, parabén foi APROVADO'.format(media))
elif 7 > media >=5:
    print('Sua média foi de {:.1f}, voce esta de RECUPEARAÇÂO '.format(media))
elif media < 5:
    print('Sua média foi de {:.1f}, voce foi REPROVADO '.format(media))

