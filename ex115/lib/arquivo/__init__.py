from lib.interface import *


def arquivoExiste(arq):
    try:
        f = open(arq, "rt")
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        f = open(arq, "wt+")
        f.close()
    except:
        print("Houve um erro na criação do Arquivo!")
    else:
        print(f"Arquivo {arq} criado com sucesso!")


def lerArquivo(arq):
    try:
        f = open(arq, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        for linha in f:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos.')
    finally:
        f.close()


def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        f = open(arq, "at")
    except:
        print("Houve um erro na abertura do arquivo!")
    else:
        try:
            f.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na escrita!")
        else:
            print(f"Novo registro de {nome} adicionado")
            f.close()
