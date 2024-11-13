# Lê a velocidade do carro
velocidade = float(input("Digite a velocidade do carro (em km/h): "))

# Verifica se a velocidade ultrapassa o limite de 80 km/h
limite_velocidade = 80
if velocidade > limite_velocidade:
    # Calcula a quantidade de km acima do limite
    km_acima = velocidade - limite_velocidade
    
    # Calcula o valor da multa (R$5 por km acima do limite)
    multa = km_acima * 5
    
    # Exibe a mensagem de multa
    print(f"Você foi multado! A velocidade ultrapassou {km_acima} km/h do limite permitido.")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    # Caso a velocidade esteja dentro do limite
    print("Você está dentro do limite de velocidade. Não foi multado.")
