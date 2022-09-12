contagem = (
    "zero",
    "um",
    "dois",
    "tres",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
while True:
    numero = int(input("digite um número entre 0 e 20: "))
    if numero >= 0 and numero <= 20:
        break
    print("Tente novamente. ", end="")
print(f'Você digitou o número {contagem[numero]}')

# for pos, cont in enumerate(contagem):
#     if numero > 20 or numero < 0:
#         print("Tente novamente. ", end="")
#         numero = int(input("digite um número entre 0 e 20: "))
#     elif numero == pos:
#         print(f"Você digitou o número {cont}")
