# Função principal
def main():
    total_altura = 0        # Soma das alturas para calcular a média
    mais_90kg = 0           # Contador de pessoas com mais de 90Kg
    menos_50kg_menos_160m = 0  # Contador de pessoas com menos de 50Kg e menos de 1.60m
    mais_190m_mais_100kg = 0   # Contador de pessoas com mais de 1.90m e mais de 100Kg
    
    # Loop para ler o peso e a altura das 7 pessoas
    for i in range(1, 8):  # De 1 a 7 (7 pessoas)
        peso = float(input(f"Digite o peso da {i}ª pessoa (em Kg): "))  # Lê o peso
        altura = float(input(f"Digite a altura da {i}ª pessoa (em metros): "))  # Lê a altura
        
        # Soma a altura ao total de alturas
        total_altura += altura
        
        # Verifica as condições para cada contagem
        if peso > 90:
            mais_90kg += 1  # Incrementa se a pessoa pesa mais de 90Kg
        
        if peso < 50 and altura < 1.60:
            menos_50kg_menos_160m += 1  # Incrementa se a pessoa pesa menos de 50Kg e tem menos de 1.60m
        
        if altura > 1.90 and peso > 100:
            mais_190m_mais_100kg += 1  # Incrementa se a pessoa mede mais de 1.90m e pesa mais de 100Kg
    
    # Calcula a média de altura
    media_altura = total_altura / 7
    
    # Exibe os resultados
    print(f"\nMédia de altura do grupo: {media_altura:.2f} metros")
    print(f"Pessoas que pesam mais de 90Kg: {mais_90kg}")
    print(f"Pessoas que pesam menos de 50Kg e têm menos de 1.60m: {menos_50kg_menos_160m}")
    print(f"Pessoas com mais de 1.90m e mais de 100Kg: {mais_190m_mais_100kg}")

# Chama a função principal
main()
