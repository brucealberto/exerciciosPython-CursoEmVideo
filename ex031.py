from math import dist


distancia = float(input("digite a distância em km: "))
if distancia <= 200:
    print(f"o valor é de R${distancia * 0.50:.2f}")
else:
    print(f"o valor é de R${distancia * 0.45:.2f}")
