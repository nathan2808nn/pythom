# Programa que exibe uma contagem até o valor informado pelo usuário
def main():
    # Solicita ao usuário um número inteiro e positivo
    numero = int(input("Digite um valor: "))
    
    # Verifica se o número é positivo
    if numero <= 0:
        print("Por favor, digite um número positivo!")
        return

    # Exibe a contagem até o valor informado
    print("Contagem:", end=" ")
    for i in range(1, numero + 1):
        print(i, end=" ")  # Exibe o número seguido de um espaço
    print("Acabou!")  # Exibe "Acabou!" ao final da contagem

# Chama a função principal
main()
