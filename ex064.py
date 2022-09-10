numero = 0
contador = 0
soma = 0
while numero != 999:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero != 999:
        soma += numero
        contador += 1
print(f"Você digitou {contador} números, e a soma entre eles foi {soma}.")
