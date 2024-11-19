# Programa para calcular a soma de 500 + 450 + 400 + ... + 0
def main():
    soma = 0  # Inicializa a soma como 0
    
    # Loop para percorrer os números de 500 até 0 com passo -50
    for i in range(500, -1, -50):
        soma += i  # Soma os números
    
    # Exibe o resultado da soma
    print(f"A soma dos números de 500 até 0 (com decremento de 50) é: {soma}")

# Chama a função principal
main()
