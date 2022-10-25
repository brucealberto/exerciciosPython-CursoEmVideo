from rich import print

jogador = {}
time = []
partidas = []
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do Jogador: ")).strip()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, total):
        jogador["gols"] = int(input(f"Quantos gols na partida {c}? "))
        partidas.append(jogador["gols"])
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        escolha = str(input("Quer continuar[S/N]? ")).strip().upper()
        if escolha in "SN":
            break
        print("ERRO! Digite S ou N. ")
    if escolha == "N":
        break
print("-=" * 30)
for k, v in enumerate(time):
    print(f"  {k:3>}", end="")
    for d in v.values():
        print(f" {str(d):<15}", end="")
    print()
print(f" {time}")
print("-=" * 30)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para sair) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! não existe jogador com códifo {busca} ")
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f"    No jogo {i + 1} fez {g} gols")
    print("-=" * 30)
print("VOLTE SEMPRE! ")
# print(f'O jogador {dados["nome"]} jogou {total} partidas. ')
# for i, v in enumerate(gols):
#     print(f"=> Na partida {i}, fez {v} gols.")
# print(f"Foi um total de {quantidade} gols. ")
