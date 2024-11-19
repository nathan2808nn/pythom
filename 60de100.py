def main():
    # Variáveis para armazenar as informações necessárias
    nome_mais_velho = ""
    idade_mais_velho = -1
    nome_mulher_jovem = ""
    idade_mulher_jovem = float('inf')  # Inicializa com um valor muito grande
    soma_idades = 0
    total_pessoas = 0
    homens_maior_30 = 0
    mulheres_menor_18 = 0

    while True:
        # Leitura dos dados
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()

        # Atualiza as estatísticas conforme os dados
        soma_idades += idade
        total_pessoas += 1

        # Verifica quem é a pessoa mais velha
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome
        
        # Verifica quem é a mulher mais jovem
        if sexo == 'F' and idade < idade_mulher_jovem:
            idade_mulher_jovem = idade
            nome_mulher_jovem = nome
        
        # Conta quantos homens têm mais de 30 anos
        if sexo == 'M' and idade > 30:
            homens_maior_30 += 1
        
        # Conta quantas mulheres têm menos de 18 anos
        if sexo == 'F' and idade < 18:
            mulheres_menor_18 += 1

        # Pergunta se o usuário quer continuar
        continuar = input("Deseja continuar? (S para sim, N para não): ").strip().upper()
        if continuar != 'S':
            break

    # Exibe os resultados
    if total_pessoas > 0:
        media_idades = soma_idades / total_pessoas
    else:
        media_idades = 0

    # Exibindo os resultados finais
    print(f"\nA pessoa mais velha é: {nome_mais_velho}, com {idade_mais_velho} anos.")
    if nome_mulher_jovem:
        print(f"A mulher mais jovem é: {nome_mulher_jovem}, com {idade_mulher_jovem} anos.")
    else:
        print("Nenhuma mulher foi cadastrada.")
    
    print(f"Média de idade do grupo: {media_idades:.2f}")
    print(f"Homens com mais de 30 anos: {homens_maior_30}")
    print(f"Mulheres com menos de 18 anos: {mulheres_menor_18}")

# Chama a função principal
main()
