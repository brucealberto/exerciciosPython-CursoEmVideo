nome_alunos = []
medias = []
while True:
    nome = str(input("Digite seu nome: ")).strip()
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    escolha = str(input("Deseja continuar? ")).strip().upper()
    media = (nota1 + nota2) / 2
    medias.append(media)
    nome_alunos.append(nome)
    if escolha in "Nn":
        break
print("-=" * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print("-" * 26)
for i, n in enumerate(nome_alunos):
    print(f"{i:<4}{n:<10}{medias[i]:>8}")
while True:
    valor = int(input("Saber a média de qual pessoa estudante? (999 exit)"))
    if valor == 999:
        print("Volte Sempre!")
        break
    if valor <= len(nome_alunos):
        print(f"a media do aluno {nome_alunos[valor]} foi de {medias[valor]}")
