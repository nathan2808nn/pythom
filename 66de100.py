# Lê o número fornecido pelo usuário
numero = int(input("Digite um valor: "))

# Usando a estrutura "para" (for) para mostrar a tabuada do número
for i in range(1, 11):  # Vai de 1 até 10
    print(f"{numero} x {i} = {numero * i}")
