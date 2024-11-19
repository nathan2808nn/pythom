# Programa que lê os valores inicial, final e incremento e faz a contagem
def main():
    # Solicita ao usuário os valores
    inicio = int(input("Digite o primeiro Valor: "))
    fim = int(input("Digite o último Valor: "))
    incremento = int(input("Digite o incremento: "))
    
    # Exibe a contagem
    print("Contagem:", end=" ")
    for i in range(inicio, fim, incremento):
        print(i, end=" ")  # Exibe o número seguido de um espaço
    print("Acabou!")  # Exibe "Acabou!" ao final da contagem

# Chama a função principal
main()
