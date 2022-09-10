frase = str(input("digite uma frase: ")).strip().upper()
vezesA = frase.count("A")
primeiraPosicao = frase.find("A") + 1
ultimaPosicao = frase.rfind("A") + 1
print(
    f'quantidade de "A" {vezesA}\nprimeira posição {primeiraPosicao}\nultima posição {ultimaPosicao}'
)
