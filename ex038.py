numero1 = int(input('digite o primeiro número: '))
numero2 = int(input('digite o segundo número: '))
if numero1 > numero2:
  print(f'\33[1;33mo primeiro número é maior')
elif numero2 > numero1:
  print(f'\33[1;36mo segundo número é maior')
else:
  print(f'\33[35mnão existe número maior , os dois são iguais')