valores = []
for posicao in range(0, 5):
    numero = int(input("Digite um número: "))
    if posicao == 0 or numero > valores[-1]:
        valores.append(numero)
        print("Adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                print(f"Adicionado na posição {pos}")
                break
            pos += 1
print(valores)
