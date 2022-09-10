from random import randint
from time import sleep

print(
    """ Suas opções :
[0] PEDRA
[1] PAPEL
[2] TESOURA"""
)
pedra = 0
papel = 1
tesoura = 2
computador = randint(0, 2)
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(0.7)
print("KEN")
sleep(0.7)
print("PO!!!")
sleep(0.7)
if computador == pedra and jogador == tesoura:
    print("Jogador jogou Tesoura!")
    print("Computador jogou Pedra!")
    print("\33[33mCOMPUTADOR VENCE!")
elif computador == papel and jogador == pedra:
    print("Jogador jogou Pedra")
    print("Computador jogou Papel!")
    print("\33[33mCOMPUTADOR VENCE!")
elif computador == tesoura and jogador == papel:
    print("Jogador jogou Papel")
    print("Computador jogou Tesoura!")
    print("\33[33mCOMPUTADOR VENCE!")
elif jogador == pedra and computador == tesoura:
    print("Jogador jogou Pedra!")
    print("Computador jogou Tesoura!")
    print("\33[31mJOGADOR VENCE!")
elif jogador == papel and computador == pedra:
    print("Jogador jogou Papel!")
    print("Computador jogou Pedra!")
    print("\33[31mJOGADOR VENCE!")
elif jogador == tesoura and computador == papel:
    print("Jogador jogou Tesoura!")
    print("Computador jogou Papel!")
    print("\33[31mJOGADOR VENCE!")
else:
    print("\33[42mdeu empate!")
