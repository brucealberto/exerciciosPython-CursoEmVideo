import moeda

valor = float(input("Digite um valor: R$"))
met = moeda.metade(valor, True)
dob = moeda.dobro(valor, True)
aum = moeda.aumentar(valor, 10, True)
dim = moeda.diminuir(valor, 13, True)
# moe = moeda.moeda(valor)
# moe_met = moeda.moeda(met)
# moe_dob = moeda.moeda(dob)
# moe_aum = moeda.moeda(aum)
# moe_dim = moeda.moeda(dim)
print(f"metade de {moeda.moeda(valor)} é => {met}")
print(f"dobro de {moeda.moeda(valor)} é => {dob}")
print(f"aumentando 10%, temos => {aum}")
print(f"reduzindo 13%, temos => {dim}")
