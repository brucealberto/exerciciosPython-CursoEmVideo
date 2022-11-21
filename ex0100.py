from random import randint


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for _cont in range(0, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n} ", end="", flush=True)


def somaPar(lista):
    par = 0
    for v in lista:
        if v % 2 == 0:
            par += v
    print(f"\nSomando os valores pares da lista {lista}, temos {par}")


numeros = list()
sorteia(numeros)
somaPar(numeros)
