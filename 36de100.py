# Função para calcular os pontos e o valor em dinheiro
def calcular_pontos_e_dinheiro(horas_atividade):
    if horas_atividade <= 10:
        pontos = horas_atividade * 2  # 2 pontos por hora para até 10h
    elif 10 < horas_atividade <= 20:
        pontos = horas_atividade * 5  # 5 pontos por hora para de 10h até 20h
    else:
        pontos = horas_atividade * 10  # 10 pontos por hora para mais de 20h

    # Calculando o valor em dinheiro
    dinheiro = pontos * 0.05  # Cada ponto vale R$ 0,05
    return pontos, dinheiro

# Função principal
def main():
    print("Bem-vindo ao sistema de cálculo de pontos e dinheiro do programa de vida saudável!")
    
    # Leitura das horas de atividade
    horas_atividade = float(input("Digite o número de horas de atividade física realizadas no mês: "))
    
    # Calcular pontos e dinheiro
    pontos, dinheiro = calcular_pontos_e_dinheiro(horas_atividade)
    
    # Exibir os resultados
    print(f"\nTotal de pontos acumulados: {pontos} pontos")
    print(f"Total de dinheiro ganho: R$ {dinheiro:.2f}")

# Chama a função principal
main()
