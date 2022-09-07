
from random import randint


computador = randint(0, 10)
palpites = 0
acertou = False
while acertou == False:
  jogador = int(input('Escolha um número: '))
  palpites += 1
  if jogador == computador:
    acertou = True
  else:
    if jogador < computador:
      print('dica... coloque Mais...')
    else:
      print('dica... coloque Menos')
print(f'Acertou!!! com {palpites} tentativas. ')