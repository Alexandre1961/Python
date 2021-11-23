'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.
Parênteses
Exponenciação
Multiplicação e divisão, que possuem a mesma precedência
Adição e subtração, que possuem a mesma precedência'''
pilha = []
exp = str(input('Digite uma expressão matemática com paremtesis:'))
print(exp)
for simb in exp:
    if simb == '(': # primeiro tem que ser este ( abre
        pilha.append(simb)
    elif simb == ')': # se achar este  )
        if len(pilha) > 0: # não ta vazia por que tem um pu mais (
            pilha.pop() # remove um (
        else: # se a pilha = 0 a exp abriu com ) ou já tem mais ) que (
            pilha.append(simb)
if len(pilha) == 0: # o final da conta de append e pop não pode ser > 1
    print(f'Sua expressão esta correta')
else:
    print(f'Sua expressão não fecha')

