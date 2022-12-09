from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(
        ["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"]
    )
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo so sistema... Até logo!")
        break
    else:
        cabeçalho("\033[31mERRO Digite uma opção válida!\033[m")
    sleep(1)

# while True:
#     resposta = menu(
#         ["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"]
#     )
#     if resposta == 1:
#         cabeçalho("resp1")
#     elif resposta == 2:1
#         cabeçalho("resp2")
#     elif resposta == 3:
#         cabeçalho("Saindo so sitema... Até logo!")
#         break
#     else:
#         cabeçalho("\033[31mERRO Digite uma opção válida!\033[m")
