from itertools import count


nome = str(input('digite seu nome completo: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
qtLetras = len(nome) - nome.count(' ')
letrasNome = len(nome.split()[0])
# letrasNome = nome.find(' ')
print(f'seu nome em maisculo {maiusculo}\nseu nome em minusculo {minusculo}\nquantas letras tem seu nome {qtLetras}\nquantidade de letras do primeiro nome {letrasNome}')