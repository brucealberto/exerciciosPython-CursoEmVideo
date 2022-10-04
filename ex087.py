from time import sleep


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = maior_valor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f"Digite um valor para: [{linha}, {coluna}] ")
        )
print('Gerando a matriz...')
sleep(1)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print(f"A soma dos valores pares é: {soma_pares} ")
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f"A soma da terceira coluna é: {soma_coluna} ")
for coluna in range(0, 3):
    if coluna == 0:
        maior_valor = matriz[1][coluna]
    elif matriz[1][coluna] > maior_valor:
        maior_valor = matriz[1][coluna]
print(f"O maior valor da segunda linha é: {maior_valor} ")
