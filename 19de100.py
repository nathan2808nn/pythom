# Lê o nome do aluno
nome = input("Digite o nome do aluno: ")

# Lê as duas notas do aluno
nota1 = float(input(f"Digite a primeira nota de {nome}: "))
nota2 = float(input(f"Digite a segunda nota de {nome}: "))

# Calcula a média do aluno
media = (nota1 + nota2) / 2

# Exibe a média do aluno
print(f"A média do aluno {nome} é: {media:.2f}")

# Analisa o desempenho do aluno
if media >= 7.0:
    print(f"{nome} teve um bom aproveitamento!")
else:
    print(f"{nome} não teve um bom aproveitamento.")
