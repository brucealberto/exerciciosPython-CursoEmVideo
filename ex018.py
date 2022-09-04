from math import sin, cos, tan, radians
angulo = float(input('digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'o ângulo de {angulo} tem o SENO de {seno:.2f}\no ângulo de {angulo} tem o COSSENO de {cosseno:.2f}\no ângulo de {angulo} tem a TANGENTE de {tangente:.2f}\n')