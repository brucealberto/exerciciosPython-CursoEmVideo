from time import sleep


valores = []
valores_pares = []
valores_impares = []
while True:
    numero = int(input("Digite um número: "))
    escolha = str(input("Deseja continuar? [S/N] "))
    valores.append(numero)
    if numero % 2 == 0:
        valores_pares.append(numero)
    else:
        valores_impares.append(numero)
    if escolha in "Nn":
        break
print("calculando...")
sleep(0.9)
print(f"Lista com os valores normais: {valores} ")
print(f"Lista com os valores Pares: {valores_pares} ")
print(f"Lista com os valores Ímpares: {valores_impares} ")
