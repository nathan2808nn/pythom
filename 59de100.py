def main():
    maior_idade = 0
    homens_count = 0
    soma_idade_homens = 0
    mulher_mais_jovem = float('inf')  # Inicializa com um valor muito grande (infinito)

    while True:
        # Solicita o sexo e a idade da pessoa
        sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()
        idade = int(input("Digite a idade da pessoa: "))

        # Atualiza a maior idade
        if idade > maior_idade:
            maior_idade = idade
        
        # Verifica o sexo e faz os cálculos necessários
        if sexo == 'M':
            homens_count += 1
            soma_idade_homens += idade
        elif sexo == 'F':
            if idade < mulher_mais_jovem:
                mulher_mais_jovem = idade
        else:
            print("Sexo inválido. Por favor, digite 'M' ou 'F'.")
            continue  # Se o sexo for inválido, repete o ciclo

        # Pergunta se o usuário deseja continuar
        continuar = input("Deseja cadastrar outra pessoa? (S para sim, N para não): ").strip().upper()
        if continuar != 'S':
            break

    # Exibe os resultados
    if homens_count > 0:
        media_idade_homens = soma_idade_homens / homens_count
    else:
        media_idade_homens = 0

    print(f"\nMaior idade lida: {maior_idade}")
    print(f"Quantos homens foram cadastrados: {homens_count}")
    
    if mulher_mais_jovem != float('inf'):
        print(f"Idade da mulher mais jovem: {mulher_mais_jovem}")
    else:
        print("Nenhuma mulher foi cadastrada.")
    
    print(f"Média de idade entre os homens: {media_idade_homens:.2f}")

# Chama a função principal
main()
