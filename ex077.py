palavras = ("chao", "pao", "loja", "comida")
vogais = "aeiou"
for p in palavras:
    print(f'\nna palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in vogais:
            print(letra, end=' ')
