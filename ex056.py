media = 0
anos = 0
mulheres = 0
homemVelho = 0
nomeHomemVelho = ""
for c in range(1, 5):
    print(f"----- {c}ª PESSOA -----")
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Qual seu sexo, M ou F? ")).strip()
    anos += idade
    media = anos / 4
    if c == 1 and sexo in "Mm":
        homemVelho = idade
        nomeHomemVelho = nome
    elif idade > homemVelho:
        homemVelho = idade
        nomeHomemVelho = nome
if sexo in "Ff" and idade < 20:
    mulheres += 1
print(f"A média de idade do grupo é de {media} anos. ")
print(f"O homem mais velho tem {homemVelho} anos e se chama {nomeHomemVelho}.")
print(f"Ao todo são {mulheres} mulhers com menos de 20 anos")
