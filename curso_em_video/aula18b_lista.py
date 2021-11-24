print(f'{" LISTA COMPOSTA ":*^40}')
pessoas = [['Alex', 60], ['Maria', 61], ['Ame', 35], ['Fefa', 34]]
print('A lista composta pessoas é ', pessoas)
print('pessoa[0][1]', pessoas[0][1])
print('pessoas[2][1]', pessoas[2][0])
print('pessoa [3][0][3]', pessoas[3][0][3])
for p in pessoas:
    print(f'{[p[0]]} tem {p[1]} anos de idade ')
print(f'{" PASSAGEM DE DADO PARA CADASTRO ":*^40}')
dado = list()
cadastro = []
for c in range(0, 5):
    dado.append(str(input('Nome: ')).strip().upper())
    dado.append(int(input('Idade: ')))
    print(f'para for c={c}, nome é {dado[0]} e idade é {dado[1]}')
    cadastro.append(dado[:])
    print(f'cadastro.append(dado[:]) é : {cadastro}')
    dado.clear()
    print(f'Após dado.clear, dado = {dado}')
print(f'{" FIM DA PASSAGEM DE DADO ":*^40}')
totmaior = totmenor = 0
for p in cadastro:
    if p[1] >= 21:
        print(f'{p[0]} é maior de {p[1]} anos')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de {p[1]} com ')
        totmenor += 1
print(f'temos {totmaior} maiores de idade e {totmenor} menores')
