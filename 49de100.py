# Programa para ler 6 números inteiros e contar quantos são pares e ímpares
def main():
    # Inicializa as variáveis para contar os números pares e ímpares
    pares = 0
    impares = 0
    
    # Loop para ler 6 números inteiros
    for i in range(1, 7):
        numero = int(input(f"Digite o {i}º número: "))  # Lê o número inteiro
        
        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            pares += 1  # Se for par, incrementa o contador de pares
        else:
            impares += 1  # Se for ímpar, incrementa o contador de ímpares
    
    # Exibe a quantidade de números pares e ímpares
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

# Chama a função principal
main()
