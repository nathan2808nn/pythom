
a = float(input("Digite o comprimento do primeiro segmento de reta: "))
b = float(input("Digite o comprimento do segundo segmento de reta: "))
c = float(input("Digite o comprimento do terceiro segmento de reta: "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        tipo = "EQUILÁTERO"
    elif a == b or a == c or b == c:
        tipo = "ISÓSCELES"
    else:
        tipo = "ESCALENO"
    
    
    print(f"É possível formar um triângulo do tipo {tipo}.")
else:
    print("Não é possível formar um triângulo com esses segmentos.")
