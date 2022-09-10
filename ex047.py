print("\33[34mOs números pares entre 1 e 50 são...")
for c in range(1, 51):
    if c % 2 == 0:
        print(f"{c} ", end="")
print("\33[4;31m fim do programa!")


# Solução Guanabara
for n in range(2, 51, 2):
    print(n, end=" ")
print("Acabou")
