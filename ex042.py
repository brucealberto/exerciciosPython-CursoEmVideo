reta1 = float(input("digite a primeira reta: "))
reta2 = float(input("digite a segunda reta: "))
reta3 = float(input("digite a terceira reta: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("pode formar um triangulo", end="")
    if reta1 == reta2 == reta3:
        print(" EQUILÁtERO!, ou seja possui todos os lados iguais")
    elif reta1 != reta2 != reta3 != reta1:
        print(" ESCALENO, ou seja todos os lados são diferentes")
    else:
        print(" ISÓSCELES, ou seja possui dois lados iguais")
else:
    print("não podem formar um triângulo...")

# if reta1 and reta2 and reta3 == reta1 and reta2 and reta3:
#   print('o triângulo é EQUILÁtERO!, ou seja possui todos os lados iguais')
# elif (reta1 == reta2) != reta3 and (reta1 == reta3) != reta2 and (reta2 == reta3) != reta1 and (reta3 == reta1) != reta2:
#   print('o triangulo é ISÓSCELES, ou seja possui dois lados iguais')
# elif (reta1 != reta2) and (reta1 != reta3) and (reta2 != reta3):
#   print('o trinângulo é ESCALENO, ou seja todos os lados são diferentes')
