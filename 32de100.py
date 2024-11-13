import random

# Função principal do jogo
def jogar():
    print("Bem-vindo ao jogo de adivinhação!")
    print("O computador vai sortear um número entre 1 e 5.")
    
    # O computador sorteia um número entre 1 e 5
    numero_sorteado = random.randint(1, 5)
    
    # O jogador tenta adivinhar
    tentativa = int(input("Tente adivinhar qual foi o número sorteado (entre 1 e 5): "))
    
    # Verifica se o jogador acertou
    if tentativa == numero_sorteado:
        print(f"Parabéns! Você acertou! O número sorteado foi {numero_sorteado}.")
    else:
        print(f"Você errou! O número sorteado foi {numero_sorteado}.")
        
# Chama a função para iniciar o jogo
jogar()
