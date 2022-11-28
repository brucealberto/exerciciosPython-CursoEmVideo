def fatorial(num=1, show=False):
    f = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end="")
            if n > 1:
                print(" x ", end="")
            else:
                print(f" = {f} ", end="\n")
        f *= n

    return f


number = int(input("Fatorial de qual número?.. "))
f1 = fatorial(number, show=True)
print(f"Fatorial de {number} é {f1} ", end='\n')
