primeiroTermo = int(input("digite o primeiro termo: "))
razao = int(input("digite a razão: "))

contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f"{primeiroTermo} -> ", end="")
        primeiroTermo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Fim do programa, a quantidade de termos utilizada foi de {total}")
