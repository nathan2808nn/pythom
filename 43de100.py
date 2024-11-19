# Programa que faz a contagem regressiva e marca os números divisíveis por 4
def main():
    # Loop para contar de 30 até 1
    for i in range(30, 0, -1):
        if i % 4 == 0:
            # Se o número for divisível por 4, exibe entre colchetes
            print(f"[{i}]", end=" ")
        else:
            # Se não for divisível por 4, apenas exibe o número
            print(i, end=" ")
    print("...")  # Finaliza com "..."

# Chama a função principal
main()
