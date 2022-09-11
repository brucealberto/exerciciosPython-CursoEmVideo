total_gasto = 0
caro = 0
contador = 0
menor = 0
# barato = ''
while True:
    nome = str(input("Digite o nome do produto: ")).strip()
    preco = float(input("Digite o valor do produto: R$"))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if continuar not in 'SN':
            print('Digite corretamente.')

    total_gasto += preco
    if preco > 1000:
        caro += 1
    contador += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = nome
    if continuar in "nN":
        break
print(f"O total ficou R${round(total_gasto)} ")
print(f"{caro} produtos custam mais de R$1000. ")
print(f"O nome do mais barato foi {barato}. e o preço foi R${round(menor)} ")
