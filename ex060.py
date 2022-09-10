# numero = int(input('Digite um número: '))
# contador = numero
# fatorial = 1
# print(f'fatorial de {numero}! = ', end='')
# while contador > 0:
#   print(f'{contador}', end='')
#   print(' x ' if contador > 1 else ' = ', end='')
#   fatorial *= contador
#   contador -= 1
# print(f'{fatorial}')

# com For

numero = int(input("Digite um número: "))
fatorial = 1
print(f"fatorial de {numero}! é :")
for c in range(numero, 0, -1):
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    fatorial *= c
print(fatorial)
