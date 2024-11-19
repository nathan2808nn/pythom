# Programa que lê os valores inicial, final e incremento e faz a contagem corretamente em qualquer situação
def main():
    # Solicita ao usuário os valores
    inicio = int(input("Digite o primeiro Valor: "))
    fim = int(input("Digite o último Valor: "))
    incremento = int(input("Digite o incremento: "))
    
    # Verifica se o incremento é válido
    if incremento == 0:
        print("O incremento não pode ser zero!")
        return
    
    # Se o incremento for positivo, a contagem é crescente
    if incremento > 0:
        if inicio >= fim:
            print("O valor inicial deve ser menor que o valor final para contagem crescente.")
            return
        # Exibe a contagem crescente
        print("Contagem:", end=" ")
        for i in range(inicio, fim, incremento):
            print(i, end=" ")
    
    # Se o incremento for negativo, a contagem é regressiva
    elif incremento < 0:
        if inicio <= fim:
            print("O valor inicial deve ser maior que o valor final para contagem regressiva.")
            return
        # Exibe a contagem regressiva
        print("Contagem:", end=" ")
        for i in range(inicio, fim, incremento):
            print(i, end=" ")
    
    print("Acabou!")  # Exibe "Acabou!" ao final da contagem

# Chama a função principal
main()
