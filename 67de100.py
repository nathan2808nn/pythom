# Lê o número fornecido pelo usuário
numero = int(input("Digite um valor: "))

# Usando a estrutura "para" (for) para mostrar a contagem de 0 até o número digitado
print("Contagem:", end=" ")

# A estrutura "for" vai de 0 até o número digitado (inclusive)
for i in range(numero + 1):
    if i < numero:
        print(i, end=", ")
    else:
        print(i, end="")

# Exibe "FIM!" no final
print(", FIM!")
