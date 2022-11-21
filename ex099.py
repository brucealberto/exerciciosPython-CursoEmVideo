# valores = [2, 3, 6, 7, 91, 23, 45]


from time import sleep


def maior(*valores):
    contador = maior = 0
    print("\nMostrando os valores... ")
    for v in valores:
        print(f"{v} ", end="", flush=True)
        sleep(0.3)
        if contador == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        contador += 1
    print(f"Foram informados {len(valores)} valores")
    print(f"O maior valor é {maior}. ")


maior(2, 3, 6, 7, 91, 23, 45)
maior(2, 3, 4, 2, 11, 73, 15, 32, 43)
maior(2, 3, 4)
maior(2, 3)
maior(2)
maior()
