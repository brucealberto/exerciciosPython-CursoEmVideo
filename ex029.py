velocidade = float(input("digite sua velocidade: "))
if velocidade > 80:
    print(
        f"\33[1;31m você foi multado 🛑, e o valor da multa é de \33[32mR${(velocidade - 80) * 7:.2f}!"
    )
else:
    print("\33[1;32m você está dentro da velocidade permitida...")
