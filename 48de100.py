# Programa para ler 7 números inteiros e mostrar o somatório entre eles
def main():
    soma = 0  # Inicializa a soma como 0
    
    # Loop para ler 7 números e somá-los
    for i in range(1, 8):  # De 1 a 7 (7 números)
        numero = int(input(f"Digite o {i}º número: "))  # Lê o número
        soma += numero  # Soma o número à variável soma
    
    # Exibe o resultado da soma
    print(f"O somatório dos números é: {soma}")

# Chama a função principal
main()
