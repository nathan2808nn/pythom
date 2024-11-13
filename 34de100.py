# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso ideal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 40:
        return "Obesidade"
    else:
        return "Obesidade mórbida"

# Função principal
def main():
    print("Bem-vindo ao calculador de IMC!")
    
    # Entrada de dados
    peso = float(input("Digite o seu peso (kg): "))
    altura = float(input("Digite a sua altura (m): "))
    
    # Cálculo do IMC
    imc = calcular_imc(peso, altura)
    
    # Classificação do IMC
    classificacao = classificar_imc(imc)
    
    # Exibição dos resultados
    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

# Chama a função principal
main()
