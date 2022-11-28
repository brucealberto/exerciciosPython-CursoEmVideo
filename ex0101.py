def voto(ano):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 18:
        print(f"Com {idade} anos: VOTO NEGADO")
    elif idade >= 18 and idade <= 60:
        print(f"Com {idade} anos: VOTO OBRIGATORIO")
    else:
        print(f"Com {idade} anos: VOTO OPCIONAL")


# Programa principal
born = int(input("Digite o ano em que você nasceu.. "))
voto(born)
