numero = int(input('digite um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'unidade:{unidade}\ndezena:{dezena}\ncentena:{centena}\nmilhar:{milhar}\n')

# numero = str(input('digite um numero entre 0 a 9999: '))
# print(f'unidade:{numero[3]}\ndezena:{numero[2]}\ncentena:{numero[1]}\nmilhar:{numero[0]}\n')