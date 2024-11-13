# Função para calcular o preço do aluguel
def calcular_aluguel(tipo_carro, dias, km_percorridos):
    # Preços do aluguel de acordo com o tipo de carro
    if tipo_carro == "popular":
        aluguel_diario = 90
        if km_percorridos <= 100:
            preco_km = 0.20
        else:
            preco_km = 0.10
    elif tipo_carro == "luxo":
        aluguel_diario = 150
        if km_percorridos <= 200:
            preco_km = 0.30
        else:
            preco_km = 0.25
    else:
        return "Tipo de carro inválido"
    
    # Cálculo do preço total
    custo_aluguel = aluguel_diario * dias
    custo_km = km_percorridos * preco_km
    total = custo_aluguel + custo_km
    return total

# Função principal
def main():
    print("Bem-vindo ao sistema de cálculo de aluguel de carros!")
    
    # Leitura dos dados de entrada
    tipo_carro = input("Digite o tipo de carro (popular ou luxo): ").lower()
    dias = int(input("Digite o número de dias de aluguel: "))
    km_percorridos = float(input("Digite o número de quilômetros percorridos: "))
    
    # Calcula o valor total do aluguel
    total = calcular_aluguel(tipo_carro, dias, km_percorridos)
    
    if isinstance(total, str):  # Se o tipo de carro for inválido
        print(total)
    else:
        # Exibe o valor total a ser pago
        print(f"O valor total a ser pago é: R$ {total:.2f}")

# Chama a função principal
main()
