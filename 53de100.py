# Função principal
def main():
    total_homens = 0      # Contador para homens
    total_mulheres = 0    # Contador para mulheres
    idade_total = 0       # Soma das idades de todos
    idade_homens = 0     # Soma das idades dos homens
    mulheres_mais_20 = 0  # Contador de mulheres com mais de 20 anos
    
    # Loop para ler as idades e sexos das 5 pessoas
    for i in range(1, 6):  # De 1 a 5 (5 pessoas)
        idade = int(input(f"Digite a idade da {i}ª pessoa: "))  # Lê a idade
        sexo = input(f"Digite o sexo da {i}ª pessoa (M/F): ").strip().upper()  # Lê o sexo
        
        # Soma a idade ao total de idades
        idade_total += idade
        
        # Verifica se a pessoa é homem ou mulher e atualiza os contadores
        if sexo == 'M':
            total_homens += 1
            idade_homens += idade  # Soma a idade dos homens
        elif sexo == 'F':
            total_mulheres += 1
            if idade > 20:
                mulheres_mais_20 += 1  # Conta mulheres com mais de 20 anos

    # Cálculos das médias
    media_idade = idade_total / 5  # Média de idade do grupo
    if total_homens > 0:
        media_idade_homens = idade_homens / total_homens  # Média de idade dos homens
    else:
        media_idade_homens = 0  # Caso não haja homens, a média será 0
    
    # Exibe os resultados
    print(f"\nTotal de homens cadastrados: {total_homens}")
    print(f"Total de mulheres cadastradas: {total_mulheres}")
    print(f"Média de idade do grupo: {media_idade:.2f}")
    print(f"Média de idade dos homens: {media_idade_homens:.2f}")
    print(f"Mulheres com mais de 20 anos: {mulheres_mais_20}")

# Chama a função principal
main()
