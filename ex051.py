primeiroTermo = int(input("digite o primeiro termo: "))
razao = int(input("digite a razão: "))
decimo = primeiroTermo + (10 - 1) * razao  # Guanabara
for c in range(primeiroTermo, decimo + 1, razao):
    print(f"{c}", end=" > ")

print("Acabou.")
