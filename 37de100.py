# Função para calcular o novo salário com base no gênero e anos de empresa
def calcular_aumento(salario, genero, anos_empresa):
    if genero == "mulher":
        if anos_empresa < 15:
            aumento = 0.05  # 5% de aumento
        elif 15 <= anos_empresa <= 20:
            aumento = 0.12  # 12% de aumento
        else:
            aumento = 0.23  # 23% de aumento
    elif genero == "homem":
        if anos_empresa < 20:
            aumento = 0.03  # 3% de aumento
        elif 20 <= anos_empresa <= 30:
            aumento = 0.13  # 13% de aumento
        else:
            aumento = 0.25  # 25% de aumento
    else:
        return "Gênero inválido"

    # Calculando o novo salário
    novo_salario = salario * (1 + aumento)
    return novo_salario

# Função principal
def main():
    print("Bem-vindo ao sistema de reajuste de salários!")

    # Leitura dos dados de entrada
    salario = float(input("Digite o salário atual do funcionário: R$ "))
    genero = input("Digite o gênero do funcionário (homem ou mulher): ").lower()
    anos_empresa = int(input("Digite quantos anos o funcionário trabalha na empresa: "))
    
    # Calcula o novo salário
    novo_salario = calcular_aumento(salario, genero, anos_empresa)
    
    if isinstance(novo_salario, str):  # Verifica se houve erro no cálculo devido ao gênero
        print(novo_salario)
    else:
        # Exibe o novo salário
        print(f"\nNovo salário: R$ {novo_salario:.2f}")

# Chama a função principal
main()
