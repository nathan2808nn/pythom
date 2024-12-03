# Criando o vetor com 8 posições
vetor = []

# Preenchendo o vetor conforme o padrão especificado
for i in range(8):
    if i == 0:
        vetor.append(999)  # Preenche a primeira linha com 999
    else:
        vetor.append(i - 1)  # Preenche a segunda linha com valores de 0 a 7

# Exibindo o vetor
print("Vetor preenchido:")
for i in range(8):
    if i == 0:
        print(999, end=" ")
    else:
        print(i - 1, end=" ")
