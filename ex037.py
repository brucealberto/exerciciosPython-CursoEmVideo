numero = int(input('digite um número: '))
conversor = int(input('escolha uma base de conversão, 1 para binário, 2 para octal e 3 para hexadecimal: '))
if conversor == 1 :
  print(f'\33[32ma base de conversão do numero {numero} para binário é {bin(numero)[2:]}')
elif conversor == 2 :
  print(f'\33[;34ma base de conversão do numero {numero} para octal é {oct(numero)[2:]}')
elif conversor == 3 :
  print(f'\33[;33m a base de conversão do numero {numero} para hexadecimal é {hex(numero)[2:]}')
else:
  print('você não escolheu uma base entre as destacadas ....')