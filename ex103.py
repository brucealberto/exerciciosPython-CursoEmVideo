def ficha(jog="<desconhecido>", gol=0):
    print(f"O Jogador {jog} fez {gol} gol(s) ..")


jogador = str(input("Nome do jogador: "))
gols = str(input("Numero de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == "":
    ficha(gol=gols)
else:
    ficha(jogador, gols)
