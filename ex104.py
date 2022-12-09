def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print("ERRO! Digite um número válido..")
        if ok:
            break
    return valor


number = leiaInt("Digite um número...")
print(f"Você digitou o número {number}")
