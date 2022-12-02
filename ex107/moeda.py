def aumentar(preco, taxa):
    calc = preco + (preco * taxa / 100)
    return calc


def diminuir(preco, taxa):
    calc = preco - (preco * taxa / 100)
    return calc


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2
