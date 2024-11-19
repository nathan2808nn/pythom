# Programa que exibe a contagem de 0 até 18 com incremento de 3
def main():
    for i in range(0, 19, 3):  # Começa em 0, vai até 18 (19 não é incluído) com passo 3
        print(i, end=" ")  # Exibe o número seguido de um espaço
    print("Acabou!")  # Exibe a palavra "Acabou!" no final

# Chama a função principal
main()
