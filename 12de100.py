# Solicita o preço do produto
preco = float(input("Digite o preço do produto: "))
# Calcula o preço promocional com 5% de desconto
desconto = preco * 0.05
preco_promocional = preco - desconto
# Exibe o resultado
print(f"O preço promocional é R${preco_promocional:.2f}.")
