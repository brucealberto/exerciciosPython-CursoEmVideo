valores = []
maior = 0
menor = 0
pos1 = 0
pos2 = 0
for posicao, valor in enumerate(range(0, 5)):
    numero = int(input(f"Digite um valor para a Posição {posicao}: "))
    valores.append(numero)
    if valor == 0:
        maior = valores[valor]
        menor = valores[valor]
    else:
        if valores[valor] > maior:
            maior = valores[valor]
            pos1 = posicao
        elif valores[valor] < menor:
            menor = valores[valor]
            pos2 = posicao

print("*" * 30)
print(f"Você digitou os valores {valores}")
print(f"O maior valor foi: {maior} na posição {pos1}")
print(f"O menor valor foi: {menor} na posição {pos2}")
