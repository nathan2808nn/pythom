# Solicita o salário do funcionário
salario = float(input("Digite o salário do funcionário: "))
# Calcula o novo salário com 15% de aumento
aumento = salario * 0.15
novo_salario = salario + aumento
# Exibe o resultado
print(f"O novo salário com 15% de aumento é R${novo_salario:.2f}.")
