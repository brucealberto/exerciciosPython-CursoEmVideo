from random import randint
from time import sleep

computador = randint(0, 5)
usuario = int(input("digite um número: "))
print("estou pensando...")
sleep(2)
if usuario == computador:
    print("usuario venceu! 😁")
else:
    print("computador venceu 💻")
