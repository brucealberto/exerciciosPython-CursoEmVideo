sexo = str(input("Informe seu sexo: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = (
        str(input("Dados inválidos. informe seu sexo corretamente: "))
        .strip()
        .upper()[0]
    )
print(f"sexo {sexo} registrado com sucesso ")
