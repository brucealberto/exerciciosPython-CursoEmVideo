maiorPeso = 0
menorPeso = 0
for pessoa in range(1, 6):
  peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
  if pessoa == 1:
    maiorPeso = peso
    menorPeso = peso
  elif peso > maiorPeso:
    maiorPeso = peso
  elif peso < menorPeso:
    menorPeso = peso 
print(f'o maior peso é {maiorPeso}, e o menor peso é {menorPeso}...')