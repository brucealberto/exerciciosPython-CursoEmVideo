pessoas = 0
homem = 0
mulher = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Digite seu sexo: [M/F] ")).strip().upper()[0]
        if sexo not in 'MF':
            print('Digite corretamente. ')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if continuar not in 'SN':
            print('Digite corretamente. ')
    if idade >= 18:
        pessoas += 1
    if sexo in "Mm":
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    if continuar in "Nn":
        break
print(f"existem {pessoas} pessoas com mais de 18 anos. ")
print(f"Foram cadastrados {homem} homens. ")
print(f"Existem {mulher} mulheres com menos de 20 anos. ")
