# Solicita o número de dias trabalhados
dias_trabalhados = int(input("Digite o número de dias trabalhados no mês: "))
# Cálculo do salário
horas_por_dia = 8
valor_por_hora = 25
salario = dias_trabalhados * horas_por_dia * valor_por_hora
# Exibe o resultado
print(f"O salário do funcionário é R${salario:.2f}.")
