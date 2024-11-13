# Lê a largura e a altura da parede
largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

# Calcula a área da parede
area = largura * altura

# Cada litro de tinta pinta 2 metros quadrados
quantidade_tinta = area / 2

# Exibe a área a ser pintada e a quantidade de tinta necessária
print(f"A área a ser pintada é: {area} m²")
print(f"A quantidade de tinta necessária é: {quantidade_tinta} litro(s)")
