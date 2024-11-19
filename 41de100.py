# Programa que exibe a contagem de 100 até 0 com decrementos de 5
def main():
    for i in range(100, -1, -5):  # Começa em 100, vai até 0 (não incluindo -1), decrementando de 5 em 5
        print(i, end=" ")  # Exibe o número seguido de um espaço
    print("Acabou!")  # Exibe a palavra "Acabou!" no final

# Chama a função principal
main()
