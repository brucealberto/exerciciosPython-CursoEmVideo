from rich import print

dados = {}
dados["nome"] = str(input("Nome do Jogador: ")).strip()
total = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
gols = []
quantidade = 0
for c in range(0, total):
    dados["gols"] = int(input(f"Quantos gols na partida {c}? "))
    quantidade += dados["gols"]
    gols.append(dados["gols"])
dados["total"] = quantidade
dados["gols"] = gols
print("-=" * 30)
print(dados)
print("-=" * 30)
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v} ")
print("-=" * 30)
print(f'O jogador {dados["nome"]} jogou {total} partidas. ')
for i, v in enumerate(gols):
    print(f"=> Na partida {i}, fez {v} gols.")
print(f"Foi um total de {quantidade} gols. ")
