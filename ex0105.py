def notas(*notas, sit=False):
    d = dict()
    d["quantidade"] = len(notas)
    d["maior"] = max(notas)
    d["menor"] = min(notas)
    d["media"] = sum(notas) / len(notas)
    if sit:
        if d["media"] >= 7:
            d["situação"] = "Aprovado"
        elif d["media"] >= 5:
            d["situação"] = "Em recuperação"
        else:
            d["situação"] = "Reprovado"
    return d


resp = notas(2.3, 2.4, 4.3, 8, 7, 4, sit=True)
print(resp)
