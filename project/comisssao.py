vendas = [100, 150, 1500, 2000, 120]
bonus = []

for venda in vendas:
    if venda > 1000:
        bonus.append(True)
    else:
        bonus.append(False)

for i in range(len(vendas)):
    if bonus[i]:
        print("O vendedor", i+1, "ganhou o bônus!")
