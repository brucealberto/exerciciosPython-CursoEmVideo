from datetime import date


anoNascimento = int(input('digite seu ano de nascimento: '))
idade = date.today().year - anoNascimento
if idade < 18:
  print(f'você têm {idade} anos faltam {18 - idade}ano(s) para se alistar!')
elif idade == 18:
  print(f'\33[31mvocê têm {idade} anos!, está na hora de se alistar!')
elif idade > 18:
  print(f'você têm {idade} anos, seu alistamento foi {date.today().year + (18 - idade)}, então já se passou {idade - 18} anos para se alistar 😑')
