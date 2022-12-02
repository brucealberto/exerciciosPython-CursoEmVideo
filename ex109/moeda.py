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
