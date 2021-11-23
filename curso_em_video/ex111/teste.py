''' Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
'''
from ex111 import utilidadescev

'''
se não tiver o import em init
from ex111.utilidadescev import moeda
from ex111.utilidadescev import dado
'''

# caso tenha o import em init  from ex111.utilidadescev import dado, moeda
import ex111.utilidadescev
# porem teria que fazer a chamada utilidadescev.moeda.resumo(p, 20, 23)

p = float(input('Digite o preço R$: '))
#print(moeda.resumo(p, 20, 23)) #aparece um none no fical do programa
utilidadescev.moeda.resumo(p, 20, 23)
