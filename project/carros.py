class Locadora:
    def __init__(self):
        self.carros = {"Chevrolet Tracker": 120, "Chevrolet Onix": 90, "Hyundai HB20": 85, "Hyundai Tucson": 120, "Fiat Uno": 60, "Fiat Mobi": 70, "Fiat Pulse": 130}

    def verificar_estoque(self):
        print("Veículos disponíveis para locação:")
        for carro in self.carros:
            print(carro)

    def alugar_veiculo(self, nome_carro, dias):
        if nome_carro in self.carros:
            preco_total = self.carros[nome_carro] * dias
            del self.carros[nome_carro]
            print(f"O carro {nome_carro} foi alugado por {dias} dias. O valor total da locação é de R${preco_total}")
        else:
            print("Este veículo não está disponível para locação.")

    def devolver_veiculo(self, nome_carro):
        if nome_carro in self.carros:
            print("Este veículo já está no estoque.")
        else:
            preco = self.carros[nome_carro]
            self.carros[nome_carro] = preco
            print(f"O carro {nome_carro} foi devolvido com sucesso.")
