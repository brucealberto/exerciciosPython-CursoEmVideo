numero = int(input("Digite a quantidade de termos que você quer: "))
termo1 = 0
termo2 = 1
print(f"{termo1} -> {termo2}", end="")
contador = 3
while contador <= numero:
    termo3 = termo1 + termo2
    print(f" -> {termo3}", end="")
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(f" Está é a sequência de Fibonacci de {numero} termos!")
