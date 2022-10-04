from random import randint
from time import sleep


quantidade = int(input("Quantos jogos para sortear?: "))
lista = []
jogos = []
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
    # print('Sorteando')
for i, j in enumerate(jogos):
    sleep(1)
    print(f"JOGO {i+1}: {j}")
