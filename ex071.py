valor = int(input("Digite o valor a ser sacado: R$"))
# total = valor
cedulas = 50
contador = 0

while True:
    if valor >= cedulas:
        valor -= cedulas
        contador += 1
    else:
        if contador > 0:
            print(f'Total de {contador} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        contador = 0
        if valor == 0:
            break
print("Fim")
