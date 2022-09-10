from datetime import date
from time import sleep


maior = 0
menor = 0
anoAtual = date.today().year
for c in range(1, 8):
    anoNascimento = int(input(f"Em que ano nasceu a \033[31m{c}ª\033[m pessoa: "))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("Calculando a quantidade de pessoas...")
sleep(1.3)
print(f"existem {maior} pessoa(s) maior(es) de idade e {menor} menor(es) de idade...")
