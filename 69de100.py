# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializando variáveis
termo_atual = primeiro_termo
soma = 0

# Mostra os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são:")
for i in range(10):
    print(termo_atual, end=" ")
    soma += termo_atual  # Acumula a soma dos termos
    termo_atual += razao  # Avança para o próximo termo da PA

# Exibe a soma de todos os termos
print(f"\nA soma dos 10 primeiros termos é: {soma}")
