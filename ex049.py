
numero = int(input('qual tabuada você quer saber?, digite um número: '))

for c in range(1, 11):
  print(f'\033[33m{numero} x {c:2} = {numero * c}')