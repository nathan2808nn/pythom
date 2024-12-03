# Inicializando variáveis
total_mulheres = 0     # Contador de mulheres
total_homens_acima_100 = 0  # Contador de homens com peso acima de 100kg
soma_peso_mulheres = 0  # Soma do peso das mulheres
maior_peso_homens = 0  # Maior peso entre os homens

# Lê os dados de 8 pessoas
for i in range(1, 9):
    print(f"\nPessoa {i}:")
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    peso = float(input("Digite o peso: "))

    if sexo == 'F':  # Se for mulher
        total_mulheres += 1
        soma_peso_mulheres += peso
    elif sexo == 'M':  # Se for homem
        if peso > 100:
            total_homens_acima_100 += 1
        if peso > maior_peso_homens:
            maior_peso_homens = peso
    else:
        print("Sexo inválido! Considerando como 'não especificado'.")
        continue  # Caso o usuário digite algo errado, o loop não para e pede novamente

# Calculando a média de peso das mulheres
if total_mulheres > 0:
    media_peso_mulheres = soma_peso_mulheres / total_mulheres
else:
    media_peso_mulheres = 0  # Caso não tenha mulheres, a média é 0

# Exibindo os resultados
print("\nResultados:")
print(f"Quantidade de mulheres cadastradas: {total_mulheres}")
print(f"Quantidade de homens com mais de 100kg: {total_homens_acima_100}")
print(f"Média de peso entre as mulheres: {media_peso_mulheres:.2f} kg")
print(f"Maior peso entre os homens: {maior_peso_homens:.2f} kg")
