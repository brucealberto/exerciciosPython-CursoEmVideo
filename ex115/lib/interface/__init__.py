def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO! digite um numero válido\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuario não digitou nenhum número inteiro!\033[m")
            return None
        else:
            return num


def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    for i, item in enumerate(lista):
        print(f"\033[33m{i+1}\033[m - \033[34m{item}\033[m")
    print(linha())
    opc = leiaInt("\033[32mSua Opção: \033[m")
    return opc


# def linha(tam=42):
#     return "-" * tam


# def cabeçalho(txt):
#     print(linha())
#     print(txt.center(42))
#     print(linha())


# def menu(lista):
#     # c = 1
#     for i, item in enumerate(lista):
#         print(f"\033[33m{i+1}\033[m - \033[34m{item}\033[m")
#         # c += 1
#     print(linha())
#     opc = leiaInt("\033[32mSua Opção: \033[m")
#     return opc


# def leiaInt(msg):
#     while True:
#         try:
#             num = int(input(msg))
#         except (ValueError, TypeError):
#             print("\033[31mERRO! digite um numero válido\033[m")
#             continue
#         except KeyboardInterrupt:
#             print("Usuario não quis informar o numero")
#             return None
#         else:
#             return num
