altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em quilos: "))
sexo = input("Digite o seu sexo (M/F): ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 50
else:
    peso_ideal = (62.1 * altura) - 44.7

print(f"O seu peso ideal é {peso_ideal:.2f} kg.")

if peso > peso_ideal:
    diferenca = peso - peso_ideal
    print(f"Você precisa emagrecer {diferenca:.2f} kg para chegar ao seu peso ideal.")
    print("Frase motivadora: Você pode conquistar qualquer coisa que queira, basta querer o suficiente!")
elif peso == peso_ideal:
    print("Parabéns, você está no seu peso ideal!")
    print("Frase motivadora: O sucesso é ir de fracasso em fracasso sem perder entusiasmo.")
else:
    diferenca = peso_ideal - peso
    print(f"Você precisa engordar {diferenca:.2f} kg para chegar ao seu peso ideal.")
    print("Frase de alerta: É importante manter uma alimentação saudável e equilibrada para evitar problemas de saúde.")
