reta1 = float(input("digite a primeira reta: "))
reta2 = float(input("digite a segunda reta: "))
reta3 = float(input("digite a terceira reta: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f"\033[4;33;40m pode formar um triângulo")
