# Solicita a quantidade de Km percorridos e os dias de aluguel
km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))
# Calcula o preço total
preco_por_dia = 90
preco_por_km = 0.20
custo_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)
# Exibe o resultado
print(f"O preço total a pagar é R${custo_total:.2f}.")
