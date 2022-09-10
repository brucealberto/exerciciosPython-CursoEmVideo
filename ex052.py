numero = int(input("digite um número inteiro: "))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print("\033[32m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print(c, end=" ")
print(f"\n\033[mO número {numero} foi divisível por {total} vezes")
if total == 2:
    print("é um número Primo!")
else:
    print("não é um número Primo")
