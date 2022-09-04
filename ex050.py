soma = 0
contador = 0
for c in range(1, 7):
  numero = int(input(f'digite o {c}° número: '))
  if numero % 2 == 0:
    soma += numero
    contador += 1
print(f'a soma dos numeros pares deu: {soma}, quantos pares existem {contador}')