digitados = 0
soma = 0
while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    digitados += 1
    soma += numero
print(f'{digitados} números foram digitados e soma entre eles é {soma} ')