meta = 50000
vendas = int(input("Informe a quantidade de unidades vendidas: "))

if vendas < meta:
    print("A meta não foi atingida e ninguém receberá bônus.")
elif vendas >= meta and vendas <= meta + 500:
    bonus = vendas * 0.05
    print(f"A meta foi atingida e os vendedores receberão um bônus de 5%, totalizando {bonus:.2f} unidades.")
else:
    bonus = vendas * 0.15
    print(f"A meta foi ultrapassada em mais de 500 unidades e os vendedores receberão um bônus de 15%, totalizando {bonus:.2f} unidades.")
