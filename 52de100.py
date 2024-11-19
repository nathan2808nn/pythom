# Função principal
def main():
    total_idades = 0  # Variável para somar as idades
    mais_de_18 = 0    # Contador para pessoas com mais de 18 anos
    menos_de_5 = 0    # Contador para pessoas com menos de 5 anos
    maior_idade = 0   # Variável para armazenar a maior idade
    
    # Loop para ler as idades das 10 pessoas
    for i in range(1, 11):  # De 1 a 10 (10 pessoas)
        idade = int(input(f"Digite a idade da {i}ª pessoa: "))  # Lê a idade
        
        # Soma a idade à variável total_idades
        total_idades += idade
        
        # Verifica se a pessoa tem mais de 18 anos
        if idade > 18:
            mais_de_18 += 1
        
        # Verifica se a pessoa tem menos de 5 anos
        if idade < 5:
            menos_de_5 += 1
        
        # Verifica se a idade atual é a maior já lida
        if idade > maior_idade:
            maior_idade = idade
    
    # Calcula a média de idade
    media_idade = total_idades / 10
    
    # Exibe os resultados
    print(f"\nMédia de idade do grupo: {media_idade:.2f}")
    print(f"Pessoas com mais de 18 anos: {mais_de_18}")
    print(f"Pessoas com menos de 5 anos: {menos_de_5}")
    print(f"A maior idade lida foi: {maior_idade}")

# Chama a função principal
main()
