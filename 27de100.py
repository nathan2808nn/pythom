# Lê as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Exibe a mensagem de acordo com a média
if media <= 4.9:
    print("REPROVADO")
elif 5.0 <= media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
