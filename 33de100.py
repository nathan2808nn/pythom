# Função para calcular o valor da prestação mensal
def calcular_prestacao(valor_casa, anos_pagamento):
    # O número de meses de pagamento
    meses = anos_pagamento * 12
    # O valor da prestação mensal
    prestacao_mensal = valor_casa / meses
    return prestacao_mensal

# Função principal para aprovação do empréstimo
def aprovar_emprestimo():
    print("Bem-vindo ao simulador de empréstimo bancário!")
    
    # Entrada de dados
    valor_casa = float(input("Digite o valor da casa: R$ "))
    salario = float(input("Digite o salário do comprador: R$ "))
    anos_pagamento = int(input("Digite em quantos anos o comprador vai pagar: "))
    
    # Calcula o valor da prestação mensal
    prestacao_mensal = calcular_prestacao(valor_casa, anos_pagamento)
    
    # Calcula o limite de 30% do salário
    limite_prestacao = salario * 0.30
    
    # Verifica se a prestação mensal excede 30% do salário
    if prestacao_mensal > limite_prestacao:
        print(f"Empréstimo negado! A prestação mensal de R$ {prestacao_mensal:.2f} ultrapassa 30% do seu salário.")
    else:
        print(f"Empréstimo aprovado! A prestação mensal será de R$ {prestacao_mensal:.2f}.")

# Chama a função para executar o programa
aprovar_emprestimo()
