from time import sleep

# print('Contagem de 1 até 10 de 1 em 1')
# for c in range(1, 11, 1):
#     print(f'{c}', end=' ')
# # sleep(1)
# print('FIM!')
# for c in range(10, -1, -2):
#     print(c)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont += passo
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é você quem escolhe. ")
ini = int(input("Início: "))
fim = int(input("Fim:    "))
pas = int(input("Passo:  "))
contador(ini, fim, pas)
