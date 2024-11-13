# Lê a largura e o comprimento do terreno
largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))

# Calcula a área do terreno
area = largura * comprimento

# Exibe a área
print(f"A área do terreno é: {area} m²")

# Classifica o terreno de acordo com a área
if area < 100:
    print("Classificação: TERRENO POPULAR")
elif 100 <= area <= 500:
    print("Classificação: TERRENO MASTER")
else:
    print("Classificação: TERRENO VIP")
