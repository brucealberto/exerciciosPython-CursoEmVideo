numero = (
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
)
print(numero)
print(f"o número nove apareceu {numero.count(9)} vezes ")
if 3 in numero:
    print(f"o número 3 foi digitado na posição {numero.index(3) + 1} ")
print("os numeros pares digitados foram ", end='')
for c in numero:
    if c % 2 == 0:
        print(c, end=' ')
