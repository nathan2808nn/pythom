# Lê o nome do cliente
nome = input("Digite seu nome: ")

# Lê o sexo do cliente
sexo = input("Digite seu sexo (M para masculino / F para feminino): ").strip().upper()

# Lê o valor das compras
valor_compras = float(input("Digite o valor das suas compras: R$ "))

# Verifica o sexo e aplica o desconto correspondente
if sexo == 'M':
    desconto = 0.05  # 5% de desconto para homens
elif sexo == 'F':
    desconto = 0.13  # 13% de desconto para mulheres
else:
    print("Sexo inválido. Apenas 'M' para masculino ou 'F' para feminino são aceitos.")
    exit()  # Encerra o programa caso o sexo seja inválido

# Calcula o valor do desconto
valor_desconto = valor_compras * desconto

# Calcula o valor final com desconto
valor_final = valor_compras - valor_desconto

# Exibe o resultado
print(f"\n{nome}, o valor das suas compras foi R$ {valor_compras:.2f}.")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Valor final com desconto: R$ {valor_final:.2f}")
