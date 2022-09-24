expressao = str(input("Escreva sua expressão: ")).strip()
pilha = []
for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Expressão correta!")
else:
    print("Expressão inválida")
