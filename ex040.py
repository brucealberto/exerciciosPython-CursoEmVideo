nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2) /2
if media < 5:
  print(f'a média das suas notas é {media:.1f} infelizmente você está reprovado... 😢')
elif media >=5 and media < 7:
  print(f'a média das suas notas é {media:.1f}, e está de recuperação... 😯')
else:
  print(f'parabéns a média das suas notas é {media:.1f}, você está aprovado! 🥳')