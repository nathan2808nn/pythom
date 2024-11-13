# Lê o nome do funcionário
nome = input("Digite o nome do funcionário: ")

# Lê o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))

# Lê o tempo de trabalho na empresa (em anos)
anos_trabalhados = int(input("Digite quantos anos o funcionário trabalha na empresa: "))

# Calcula o reajuste de acordo com o tempo de trabalho
if anos_trabalhados <= 3:
    aumento = 0.03  # 3% de aumento
elif 3 < anos_trabalhados <= 10:
    aumento = 0.125  # 12.5% de aumento
else:
    aumento = 0.20  # 20% de aumento

# Calcula o novo salário
novo_salario = salario + (salario * aumento)

# Exibe o resultado
print(f"\nFuncionário: {nome}")
print(f"Salário atual: R$ {salario:.2f}")
print(f"Tempo de trabalho: {anos_trabalhados} anos")
print(f"Novo salário (após o reajuste): R$ {novo_salario:.2f}")
