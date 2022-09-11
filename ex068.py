from random import randint


# vitorias = 0
# while True:
#     computador = randint(0, 10)
#     jogador = int(input("digite um número: "))
#     valor = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
#     total = (jogador + computador) % 2 == 0
#     if total:
#         vitorias += 1
#         print(
#             f"você jogou {jogador} e o computador {computador}. "
#             + f"Total de {jogador + computador} DEU PAR"
#         )
#         print('''Você VENCEU!
#     Vamos jogar novamente...''')
#     else:
#         if jogador != total:
#             print("Você PERDEU!")
#         break
# print(f'GAME OVER! Você ganhou {vitorias} vezes')
vitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input("digite um número: "))
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print(f"você jogou {jogador} e o pc jogou {computador}.Total{total} ")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU!")
            vitorias += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("você VENCEU!")
            vitorias += 1
        else:
            print("você PERDEU!")
            break
    print("Vamos jogar novamente")
print(f"Game Over! você venceu {vitorias} vezes")
