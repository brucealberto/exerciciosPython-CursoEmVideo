quantidadeDias = float(input('qual a quantidade de dias? '))
quantidadeKm = float(input('qual a quantidade km percorridos? '))
diasRodados = 60 * quantidadeDias
kmRodados = quantidadeKm * 0.15
precoTotal = diasRodados + kmRodados
print(f'o total a pagar é de R${precoTotal:.2f}')