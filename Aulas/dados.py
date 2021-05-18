import csv


def carregar_acessos():
    X = []
    Y = []

    arquivo = open('../Arquivos/acesso.csv', 'r')
    leitor = csv.reader(arquivo)

    next(leitor)

    for home, como_funciona, contato, comprou in leitor:
        X.append([int(home), int(como_funciona), int(contato)])
        Y.append(int(comprou))

    return X, Y

def carregar_buscas():
    X = []
    Y = []

    arquivo = open('../Arquivos/buscas.csv', 'r')
    leitor = csv.reader(arquivo)

    next(leitor)

    for home, busca, logado, comprou in leitor:
        X.append([int(home), busca, int(logado)])
        Y.append(int(comprou))

    return X, Y