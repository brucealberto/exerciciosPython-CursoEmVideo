produtos = ('pão', 4, 'margarina', 2.90, 'biscoito', 1.99, 'batata', 14.90)
print(f'{"Listagem de preços":^30}')
for prod in range(0, len(produtos)):
    if prod % 2 == 0:
        print(f'{produtos[prod]:.<30}', end='')
    else:
        print(f'R${produtos[prod]:>7.2f}')