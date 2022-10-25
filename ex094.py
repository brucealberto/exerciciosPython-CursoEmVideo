from rich import print

pessoa = {}
media = soma = 0
todo_mundo = []
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Digite seu nome: ")).strip()
    while True:
        pessoa["sexo"] = str(input("Digite seu sexo [M/F]: ")).strip().upper()
        if pessoa["sexo"] in "MF":
            break
        print("Erro digite apenas m ou f ")
    pessoa["idade"] = int(input("Digite sua idade: "))
    soma += pessoa["idade"]
    todo_mundo.append(pessoa.copy())
    while True:
        escolha = str(input("Quer continuar? [S/N] ")).strip().upper()
        if escolha in "SN":
            break
        print("Digite apenas S ou N. ")
    if escolha == "N":
        break
media = soma / len(todo_mundo)
print("-=" * 30)
print(f"Ao todo foram cadastradas {len(todo_mundo)} pessoas. ")
print("As mulheres cadastradas foram", end="")
for v in todo_mundo:
    if v["sexo"] in "Ff":
        print(f' {v["nome"]}.. ', end="")
print(f"A média de idade das pessoas é {media:.1f}")
print("Pessoas acima da média.  ", end="")
for v in todo_mundo:
    if v["idade"] >= media:
        print("   ", end="")
        for k, v in v.items():
            print(f"{k} = {v}; ", end="")
        print()

# print(f'Foram cadastradas {mulheres} mulheres. ')
