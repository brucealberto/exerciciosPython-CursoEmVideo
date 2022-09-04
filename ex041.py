from datetime import date


anoNascimento = int(input('digite o ano que você nasceu: '))
idade = date.today().year - anoNascimento
if idade <= 9:
  print(f'você tem {idade} anos, sua categoria é MIRIM')
elif idade <= 14:
  print(f'você tem {idade} anos, sua categoria é INFANTIL')
elif idade <= 19:
  print(f'você tem {idade} anos, sua categoria é JUNIOR')
elif idade <= 25:
  print(f'você tem {idade} anos, sua categoria é SÊNIOR')
else:
  print(f'você tem {idade} anos, sua categoria é MASTER')