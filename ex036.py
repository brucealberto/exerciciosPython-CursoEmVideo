valorCasa = float(input('digite o valor da casa: R$'))
salario = float(input('digite seu salário: R$'))
qtAnos = int(input('digite a quantidade de anos para pagar: '))
prestacao = valorCasa / (qtAnos * 12)
if prestacao > (salario * 30/100) :
  print('infelizmente o empréstimo foi negado! ')
else:
  print('empréstimo aprovado!')