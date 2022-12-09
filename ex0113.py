def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: digite um número inteiro válido!.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuario não digitou nenhum número inteiro!\033[m")
            return None
        else:
            return num


def leiaReal(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: digite um número real válido!.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsurio preferiu não digitar um numero real\033[m")
            return None
        else:
            return num


inteiro = leiaInt("Digite um numero Inteiro: ")
real = leiaReal("Digite um número Real: ")
print(f"O numero inteiro digitado foi {inteiro} e o real foi {real} ")
