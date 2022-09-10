valorProduto = float(input("digite o valor do produto: R$"))
condicao10 = valorProduto - (valorProduto * 10 / 100)
condicao5 = valorProduto - (valorProduto * 5 / 100)
condicaoCartao = valorProduto / 2

print(
    """FORMA DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão """
)
opcao = int(input("escolha uma opção... "))
if opcao == 1:
    print(f"sua compra é de {valorProduto:.2f}, vai custar R${condicao10:.2f} no final")
elif opcao == 2:
    print(f"sua compra é de {valorProduto:.2f}, vai custar R${condicao5:.2f} no final")
elif opcao == 3:
    print(
        f"sua compra é de {valorProduto:.2f}, vai custar R${condicaoCartao:.2f} no final"
    )
elif opcao == 4:
    parcelas = int(input("quantas parcelas?... "))
    condicaoCartaoJuros = (valorProduto / parcelas) + (
        valorProduto / parcelas * 20 / 100
    )
    if parcelas == 1:
        print(f"parcelado de {parcelas}x fica: R${valorProduto / parcelas}")
    elif parcelas == 2:
        print(f"parcelado de {parcelas}x fica: R${valorProduto / parcelas}")
    else:
        print(f"parcelando de {parcelas:.2f}x fica: R${condicaoCartaoJuros} com juros!")
        print(
            f"sua compra de {valorProduto:.2f} vai custar R${parcelas * condicaoCartaoJuros:.2f}  ao final"
        )
else:
    print("opção inválida! ")
