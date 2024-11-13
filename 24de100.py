# Lê a distância que o passageiro deseja percorrer
distancia = float(input("Digite a distância que deseja percorrer em Km: "))

# Calcula o preço da passagem
if distancia <= 200:
    preco = distancia * 0.50  # R$0.50 por Km para viagens até 200Km
else:
    preco = distancia * 0.45  # R$0.45 por Km para viagens acima de 200Km

# Exibe o preço da passagem
print(f"O preço da sua passagem é: R$ {preco:.2f}")
