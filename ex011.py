largura = float(input('digite a largura em metros: '))
altura = float(input('digite a altura em metros: '))
area = largura * altura
tinta = area / 2

print(f'a area da parede é {area:.1f} m2\npara pintar a parede serão necessários {tinta:.1f}l de tinta.')
