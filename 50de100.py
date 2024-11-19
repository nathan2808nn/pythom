import random

# Função principal
def main():
    numeros_sorteados = []  # Lista para armazenar os números sorteados
    acima_de_5 = 0  # Contador para números acima de 5
    divisiveis_por_3 = 0  # Contador para números divisíveis por 3
    
    # Sorteio de 20 números entre 0 e 10
    for _ in range(20):
        numero = random.randint(0, 10)  # Sorteia um número entre 0 e 10
        numeros_sorteados.append(numero)  # Adiciona o número na lista
        
        # Verifica se o número está acima de 5
        if numero > 5:
            acima_de_5 += 1
        
        # Verifica se o número é divisível por 3
        if numero % 3 == 0:
            divisiveis_por_3 += 1
    
    # Exibe os números sorteados
    print(f"Números sorteados: {numeros_sorteados}")
    
    # Exibe quantos números estão acima de 5
    print(f"Quantidade de números acima de 5: {acima_de_5}")
    
    # Exibe quantos números são divisíveis por 3
    print(f"Quantidade de números divisíveis por 3: {divisiveis_por_3}")

# Chama a função principal
main()
