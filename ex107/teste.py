import moeda

valor = float(input("Digite um valor: R$"))
met = moeda.metade(valor)
dob = moeda.dobro(valor)
aum = moeda.aumentar(valor, 10)
dim = moeda.diminuir(valor, 13)
print(f"metade de R${valor} é => {met}")
print(f"dobro de R${valor} é => {dob}")
print(f"aumentando 10%, temos => R${aum}")
print(f"reduzindo 13%, temos => R${dim}")
