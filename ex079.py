numeros_cadastrados = []
while True:
    numero = int(input("Digite o valor: "))
    if numero in numeros_cadastrados:
        print(f"O número {numero} já existe...")
    else:
        numeros_cadastrados.append(numero)
        print("Valor adicionado com sucesso...")
    escolha = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if escolha in "Nn":
        break

numeros_cadastrados.sort()
print(numeros_cadastrados)
