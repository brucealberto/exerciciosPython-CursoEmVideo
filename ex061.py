print("-=" * 10)
primeiroTermo = int(input("digite o primeiro termo: "))
razao = int(input("digite a razão: "))

contador = 1
while contador <= 10:
    print(f"{primeiroTermo} -> ", end="")
    primeiroTermo += razao
    contador += 1
print("Fim do Programa...")
