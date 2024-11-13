# Lê os comprimentos dos três segmentos de reta
a = float(input("Digite o comprimento do primeiro segmento de reta: "))
b = float(input("Digite o comprimento do segundo segmento de reta: "))
c = float(input("Digite o comprimento do terceiro segmento de reta: "))

# Verifica se é possível formar um triângulo
if a + b > c and a + c > b and b + c > a:
    print("É possível formar um triângulo com esses segmentos.")
else:
    print("Não é possível formar um triângulo com esses segmentos.")
