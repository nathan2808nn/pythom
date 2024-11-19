# Inicializando variáveis
total_idades = 0  # Contador para o total de idades
soma_idades = 0   # Acumulador para a soma das idades
maiores_21 = 0    # Contador para pessoas com 21 anos ou mais

# Inicia o loop
while True:
    # Lê a idade da pessoa
    idade = int(input("Digite a idade: "))
    
    # Atualiza os contadores
    total_idades += 1
    soma_idades += idade
    
    if idade >= 21:
        maiores_21 += 1
    
    # Pergunta se o usuário deseja continuar
    continuar = input("Você deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break  # Sai do loop se o usuário não quiser continuar

# Calculando a média das idades
if total_idades > 0:
    media_idades = soma_idades / total_idades
else:
    media_idades = 0  # Caso não tenha sido digitado nenhuma idade

# Exibe os resultados
print("\nResultados:")
print(f"Total de idades digitadas: {total_idades}")
print(f"Média das idades: {media_idades:.2f}")
print(f"Pessoas com 21 anos ou mais: {maiores_21}")
