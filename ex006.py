from math import sqrt


number = int(input("digite um número: "))
print(
    f"""o dobro de {number} é {number * 2}
    seu triplo é {number * 3}
    e sua raiz quadrada {sqrt(number):.2f}"""
)
