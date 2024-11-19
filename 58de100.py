# Função principal
def main():
    soma_idades = 0  # Acumulador para as idades
    contador = 0     # Contador de alunos
    
    while True:
        # Solicita a idade do aluno
        idade = int(input("Digite a idade do aluno (ou 999 para sair): "))
        
        # Verifica se a idade digitada é 999 para encerrar o programa
        if idade == 999:
            break
        
        # Acumula a idade e incrementa o contador
        soma_idades += idade
        contador += 1
    
    # Verifica se o contador é maior que 0 para evitar divisão por 0
    if contador > 0:
        media_idade = soma_idades / contador
        print(f"\nNúmero de alunos na turma: {contador}")
        print(f"Média de idade da turma: {media_idade:.2f}")
    else:
        print("Nenhuma idade foi cadastrada.")

# Chama a função principal
main()
