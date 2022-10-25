aluno = {}
aluno["nome"] = str(input("Nome: ")).strip()
aluno["media"] = float(input(f'Média da pessoa estudante {aluno["nome"]}: '))
if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"
print("-=" * 30)
for k, v in aluno.items():
    print(f"- {k} é igual a {v}")
