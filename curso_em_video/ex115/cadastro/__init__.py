def arquivoExiste(nome):
    try:
        f = open(nome, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        f = open(nome, 'wt+')
        f.close()
    except:
        print(f'\033[31mERRO ao criar arquivo {nome}\033[m]')
    else:
        print(f'\033[32mArquivo {nome} pronto para uso\033[m')

def mostra(nome):
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
    except FileNotFoundError:
        print('Não foi possivel abrir o arquivo')
    else:
        print(arquivo.read())
        arquivo.close()

def inclui(nome):
    seuNome = str(input('Digite um nome: ')).strip().upper().ljust(20, '.')
    idade = str(input('Digite a idade')).strip()
    arquivo = open(nome, 'at', encoding='utf-8')
    arquivo.write(seuNome)
    arquivo.write(idade)
    arquivo.write(' anos\n')
    arquivo.close()


def altera():
    print('altera')


def exclui():
    print('exclui')



