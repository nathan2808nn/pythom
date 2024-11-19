# Programa que exibe a contagem regressiva
def main():
    for i in range(10, 2, -1):  # A contagem vai de 10 até 3 (2 não é incluído)
        print(i, end=" ")  # Exibe o número seguido de um espaço
    print("Acabou!")  # Exibe a palavra "Acabou!" no final

# Chama a função principal
main()
