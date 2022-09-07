
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:

  print('''MENU:
  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa''')
  opcao = int(input('Escolha uma opção: '))
  if opcao == 1:
    soma = numero1 + numero2
    print(f'a soma entre {numero1} + {numero2} é {soma}')
  elif opcao == 2:
    mult = numero1 * numero2
    print(f'o resultado de {numero1} x {numero2} é {mult}')
  elif opcao == 3:
    if numero1 > numero2:
      maior = numero1
    else:
      maior = numero2
    print(f'entre {numero1} e {numero2} o maior valor é {maior}')
  elif opcao == 4:
    print('Informe os números novamente: ')
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
  elif opcao == 5:
    print('Fim do programa , volte sempre! ')
  else:
    print('opção inválida. Tente novamente')