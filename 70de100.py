# Inicializa os primeiros dois termos da sequência
a, b = 1, 1

# Mostra os 10 primeiros termos da Sequência de Fibonacci
print("Os 10 primeiros termos da Sequência de Fibonacci são:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b  # Atualiza os valores de a e b
    
