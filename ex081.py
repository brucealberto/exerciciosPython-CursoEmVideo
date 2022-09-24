valores = []
quantidade = 0
while True:
    numero = int(input("Digite um número: "))
    escolha = str(input("Quer continuar: [S/N] ")).strip().upper()
    quantidade += 1
    valores.append(numero)
    valores.sort(reverse=True)
    if escolha in "Nn":
        break
print(f"Foram digitados {quantidade} numeros")
print(f"Valores organizados de forma decrescente {valores}")
if 5 in valores:
    print("O número 5 faz parte da lista. ")
else:
    print("O número 5 não está na lista...")
