from random import randint

valores = (
    (randint(1, 10)),
    (randint(1, 10)),
    (randint(1, 10)),
    (randint(1, 10)),
    (randint(1, 10)),
)
menor = 0
maior = 0

print("os valores sorteados foram: ", end="")
for valor in valores:
    print(f"{valor} ", end="")
print(f"\no menor valor foi {min(valores)}")
print(f"o maior valor foi {max(valores)}")
