temp = []
principal = []
maior = 0
menor = 0
while True:
    nome = str(input("Digite seu nome: ")).strip()
    peso = float(input("Digite seu peso: Kg "))
    escolha = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    temp.append(nome)
    temp.append(peso)
    if len(principal) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()

    if escolha in "Nn":
        break
print(principal)
print(f"Foram cadastradas {len(principal)} pessoas. ")
for p in principal:
    if p[1] == maior:
        print(f"As pessoas com maior peso são: {p[0]}")
for p in principal:
    if p[1] == menor:
        print(f"As pessoas com menor peso são: {p[0]} com {menor}")
