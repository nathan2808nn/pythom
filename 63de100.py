# Inicializando as variáveis
soma = 0          # Acumulador para a soma dos valores
menor_valor = None # Inicializa a variável para o menor valor (ainda não foi digitado)
total_valores = 0  # Contador de quantos valores foram digitados
pares = 0          # Contador de números pares

# Inicia o loop
while True:
    # Lê um número do usuário
    numero = int(input("Digite um número: "))
    
    # Atualiza os contadores
    soma += numero
    total_valores += 1
    
    # Verifica se o número é o menor valor até agora
    if menor_valor is None or numero < menor_valor:
        menor_valor = numero
    
    # Verifica se o número é par
    if numero % 2 == 0:
        pares += 1
    
    # Pergunta se o usuário deseja continuar
    continuar = input("Você deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break  # Sai do loop se o usuário não quiser continuar

# Calculando a média, caso pelo menos um número tenha sido digitado
if total_valores > 0:
    media = soma / total_valores
else:
    media = 0  # Se nenhum número foi digitado, a média é 0

# Exibe os resultados
print("\nResultados:")
print(f"Somatório de todos os valores: {soma}")
print(f"Menor valor digitado: {menor_valor}")
print(f"Média dos valores: {media:.2f}")
print(f"Quantidade de números pares: {pares}")
