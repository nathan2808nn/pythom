# Lê os comprimentos dos três segmentos de reta
a = float(input("Digite o comprimento do primeiro segmento de reta: "))
b = float(input("Digite o comprimento do segundo segmento de reta: "))
c = float(input("Digite o comprimento do terceiro segmento de reta: "))

# Verifica se é possível formar um triângulo
if a + b > c and a + c > b and b + c > a:
    # Se for possível, determina o tipo de triângulo
    if a == b == c:
        tipo = "EQUILÁTERO"
    elif a == b or a == c or b == c:
        tipo = "ISÓSCELES"
    else:
        tipo = "ESCALENO"
    
    # Exibe a mensagem de que é possível formar um triângulo e o tipo
    print(f"É possível formar um triângulo do tipo {tipo}.")
else:
    print("Não é possível formar um triângulo com esses segmentos.")
