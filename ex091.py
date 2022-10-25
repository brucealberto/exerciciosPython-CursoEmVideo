from operator import itemgetter
from random import randint
from time import sleep

maior = 0
jogo = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
}
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado. ")
    sleep(1)
ganhadores = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("="*30)
print(f'{"GANHADORES":.^30}')
sleep(1)
for i, v in enumerate(ganhadores):
    print(f"{i + 1}ºlugar: {v[0]} com {v[1]}")
    sleep(0.8)
