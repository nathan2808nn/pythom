# Função principal
def main():
    total_homens = 0  # Soma dos salários pagos aos homens
    total_mulheres = 0  # Soma dos salários pagos às mulheres
    
    while True:
        # Solicita os dados do funcionário
        salario = float(input("Digite o salário do funcionário: R$ "))
        sexo = input("Digite o sexo do funcionário (M para masculino, F para feminino): ").strip().upper()

        # Verifica se o sexo informado é válido
        if sexo not in ['M', 'F']:
            print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
            continue

        # Acumula os salários conforme o sexo
        if sexo == 'M':
            total_homens += salario
        elif sexo == 'F':
            total_mulheres += salario

        # Pergunta se o usuário deseja continuar
        continuar = input("Deseja continuar? (S para sim, N para não): ").strip().upper()
        if continuar != 'S':
            break

    # Exibe os resultados finais
    print(f"\nTotal de salários pagos aos homens: R$ {total_homens:.2f}")
    print(f"Total de salários pagos às mulheres: R$ {total_mulheres:.2f}")

# Chama a função principal
main()
