print('A soma dos números ímpares e que são múltiplos de três, e que estão no intervalo de 1 até 500 é...')
soma = 0
contador = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
    soma += c
    contador += 1
print(soma)
print(contador)