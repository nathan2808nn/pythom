# Função principal
def main():
    # Inicializa as variáveis para armazenar os preços
    maior_preco = float('-inf')  # Valor inicial muito baixo (menor que qualquer preço)
    menor_preco = float('inf')   # Valor inicial muito alto (maior que qualquer preço)
    
    # Loop para ler os preços dos 8 produtos
    for i in range(1, 9):  # De 1 a 8 (8 produtos)
        preco = float(input(f"Digite o preço do {i}º produto: R$ "))  # Lê o preço do produto
        
        # Verifica se o preço atual é maior que o maior preço registrado
        if preco > maior_preco:
            maior_preco = preco
        
        # Verifica se o preço atual é menor que o menor preço registrado
        if preco < menor_preco:
            menor_preco = preco
    
    # Exibe o maior e o menor preço
    print(f"O maior preço digitado foi: R$ {maior_preco:.2f}")
    print(f"O menor preço digitado foi: R$ {menor_preco:.2f}")

# Chama a função principal
main()
