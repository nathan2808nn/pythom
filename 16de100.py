# Solicita a quantidade de cigarros fumados por dia e quantos anos fumou
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Quantos anos você fumou? "))
# Calcula a redução de vida em minutos
minutos_perdidos_por_cigarro = 10
total_cigarros = cigarros_por_dia * 365 * anos_fumando
tempo_perdido = total_cigarros * minutos_perdidos_por_cigarro
# Converte para dias
dias_perdidos = tempo_perdido / (60 * 24)
# Exibe o resultado
print(f"Você perderá aproximadamente {dias_perdidos:.2f} dias de vida.")
