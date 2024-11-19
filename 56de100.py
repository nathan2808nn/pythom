# Função principal
def main():
    soma = 0  # Variável para armazenar o somatório dos números
    while True:
        # Lê um número inteiro do usuário
        numero = int(input("Digite um número (ou 1111 para sair): "))
        
        # Verifica se o número digitado é o 1111 para encerrar o loop
        if numero == 1111:
            break
        
        # Soma o número digitado ao total
        soma += numero
    
    # Exibe o somatório final
    print(f"O somatório dos números digitados é: {soma}")

# Chama a função principal
main()
