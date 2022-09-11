while True:
    numero = int(input("Quer ver a tabuada de qual número: "))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f"{numero} x {c} = {numero * c}")
print(
    """Você digitou um número negativo...
    Fim do programa."""
)
