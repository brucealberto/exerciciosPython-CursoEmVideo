larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))


def area(largura, comprimento):
    metros = largura * comprimento
    print(f"A área de um terreno {larg}x{comp} é de {metros}m²")


area(larg, comp)
