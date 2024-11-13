def Media(nota1, nota2):
    # Calcula a média entre as duas notas
    return (nota1 + nota2) / 2

def Situacao(media):
    # Verifica a situação do aluno com base na média
    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

# Programa principal
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

# Calculando a média
media_aluno = Media(nota1, nota2)

# Verificando a situação do aluno com base na média
situacao = Situacao(media_aluno)

# Exibindo o resultado
print(f"A média do aluno é: {media_aluno:.2f}")
print(f"Situação do aluno: {situacao}")
