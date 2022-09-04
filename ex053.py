frase = str(input('\033[34mdigite uma frase: ')).strip().upper()
fraseSeparada = frase.split()
fraseSemEspaco = ''.join(fraseSeparada)
fraseInvertida = fraseSemEspaco[::-1]
# Solução normal
# for letra in range(len(fraseSemEspaco) - 1, -1, -1):
#   fraseInvertida += fraseSemEspaco[letra]
# if fraseSemEspaco == fraseInvertida:
#   print('Temos um Palíndormo!')
# else:
#   print('Não é um Palíndromo.')

# Solução enxuta
if fraseSemEspaco == fraseInvertida:
  print('Temos um Palíndormo!')
else:
   print('Não é um Palíndromo.')
