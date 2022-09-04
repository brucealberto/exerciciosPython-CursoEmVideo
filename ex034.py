salario = float(input('digite seu salário: R$'))
if salario <= 1250:
  print(f'o aumento é de R${salario + (salario * 0.15):.2f}')
else:
  print(f'o aumento é de R${salario + (salario * 0.10):.2f}')