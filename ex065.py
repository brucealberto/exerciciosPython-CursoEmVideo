resp = "S"
contador = 0
soma = 0
maior = 0
while resp in "Ss":
    numero = int(input("Digite um número: "))
    contador += 1
    soma += numero
    media = soma / contador
    if numero > maior:
        maior = numero
    elif numero < maior:
        menor = numero
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
print(f"Você digitou {contador} números e a média foi {media:.2f} ")
print(f"O maior valor foi {maior} e o menor foi {menor} ")
