from math import hypot


catetoOposto = float(input('digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f'o comprimento da hipotenusa é = {hipotenusa:.2f}')
# hipotenusa = pow(catetoOposto, 2) + pow(catetoAdjacente, 2) 
# print(f'o comprimeto da hipotenusa de um triângulo retângulo é {sqrt(hipotenusa):.2f}')