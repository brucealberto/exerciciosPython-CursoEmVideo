def aumentar(preco=0, taxa=0):
    calc = preco + (preco * taxa / 100)
    return calc


def diminuir(preco=0, taxa=0):
    calc = preco - (preco * taxa / 100)
    return calc


def dobro(preco=0):
    return preco * 2


def metade(preco=0):
    return preco / 2


def moeda(preco=0, cifrao="R$"):
    return f"{cifrao}{preco:.2f}".replace(".", ",")
