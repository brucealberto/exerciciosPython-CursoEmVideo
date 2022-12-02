def aumentar(preco=0, taxa=0, formato=False):
    calc = preco + (preco * taxa / 100)
    if formato:
        return moeda(calc)
    else:
        return calc


def diminuir(preco=0, taxa=0, formato=False):
    calc = preco - (preco * taxa / 100)
    if formato:
        return moeda(calc)
    else:
        return calc


def dobro(preco=0, formato=False):
    if formato:
        return moeda(preco * 2)
    else:
        return preco * 2


def metade(preco=0, formato=False):
    if formato:
        return moeda(preco / 2)
    else:
        return preco / 2


def moeda(preco=0, cifrao="R$"):
    return f"{cifrao}{preco:.2f}".replace(".", ",")


def resumo(preco=0, aumento=10, reducao=5):
    print("-" * 30)
    print("RESUMO".center(30))
    print("-" * 30)
    print(f"    Preço analisado: \t{moeda(preco)}")
    print(f"    Dobro do preço: \t{dobro(preco, True) }")
    print(f"    Metade do preço: \t{metade(preco, True)}")
    print(f"    {aumento}% de aumento: \t{aumentar(preco, aumento, True)}")
    print(f"    {reducao}% de redução: \t{diminuir(preco, reducao, True)}")
    print("-" * 30)
    print("O Bruce é incrivel...".center(30))
    print("-" * 30)
