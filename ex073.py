tabela = (
    "Palmeiras",
    "Internacional",
    "Flamengo",
    "Fluminense",
    "Corinthias",
    "Atletico-PR",
    "Atletico-MG",
    "America-MG",
    "Goias",
    "Santos",
    "Bragantino",
    "Botafogo",
    "São Paulo",
    "Ceará SC",
    "Fortaleza",
    "Coritiba",
    "Cuiabá",
    "Avaí",
    "Atletico-GO",
    "Juventude",
)
# for pos, time in enumerate(tabela):
# posicao = tabela.index('Cuiabá')
print(f"A) Os 5 primeiros colocados são: {tabela[0:5]}")
print(f"B) Os 4 ultimos são: {tabela[-4:]}")
print(f"C) A lista em ordema alfábetica: {sorted(tabela)}")
print(f'D) O Cuiabá esta na {tabela.index("Cuiabá") + 1}ª posição')
