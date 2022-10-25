from datetime import date


dados = {}
dados["nome"] = str(input("Digite seu nome: ")).strip()
nasc = int(input("Digite seu ano de nascimento: "))
dados["idade"] = date.today().year - nasc
dados["ctps"] = int(input("carteira de trabalho (0 não tem): "))
if dados["ctps"] != 0:
    dados["ano_cont"] = int(input("Digite seu ano de contratação: "))
    dados["salario"] = float(input("Informe seu salário: "))
    dados["aposentadoria"] = dados["idade"] + (
        (dados["ano_cont"] + 35) - date.today().year
    )
for k, v in dados.items():
    print(f"  - {k} tem o valor {v}")
