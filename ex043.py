peso = float(input('digite seu peso: (Kg) '))
altura = float(input('digite sua altura: (m) '))
imc = peso / pow(altura, 2)
if imc < 18.5:
  print(f'seu IMC é {imc:.1f} , então você está abaixo do peso! 🙄 ')
elif imc >= 18.5 and imc < 25:
  print(f'\33[32mseu IMC é {imc:.1f}, então você está no peso ideal! 😁 ')
elif imc >= 25 and imc <= 30:
  print(f'\33[33mseu IMC é {imc:.1f}, você está com sobrepeso! 😯 ')
elif imc >= 30 and imc <= 40:
  print(f'\33[35mseu IMC é {imc:.1f}, você está com obesidade! 😥 ')
else:
  print(f'\33[31mseu IMC é {imc:.1f}, você está com obesidade mórbida! 😫 ')