# Programa para calcular a soma de 6 + 8 + 10 + ... + 100
def main():
    soma = 0  # Inicializa a soma como 0
    
    # Loop para percorrer os números de 6 até 100 com passo 2 (números pares)
    for i in range(6, 101, 2):
        soma += i  # Soma os números pares
    
    # Exibe o resultado da soma
    print(f"A soma dos números de 6 até 100 (com incremento de 2) é: {soma}")

# Chama a função principal
main()
