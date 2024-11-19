import random

# Função principal do jogo
def main():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("O computador sorteou um número entre 1 e 10, e você tem 4 tentativas para acertar.")
    
    # Sorteia um número aleatório entre 1 e 10
    numero_sorteado = random.randint(1, 10)
    
    tentativas = 4  # O jogador tem 4 tentativas

    # Loop que permite até 4 tentativas
    for tentativa in range(1, tentativas + 1):
        # Solicita ao jogador que digite um número
        palpite = int(input(f"Tentativa {tentativa}/{tentativas}. Digite seu palpite: "))

        # Verifica se o palpite está correto
        if palpite == numero_sorteado:
            print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativa} tentativas!")
            break  # Se o jogador acertar, o jogo termina
        elif palpite < numero_sorteado:
            print("O número sorteado é maior! Tente novamente.")
        else:
            print("O número sorteado é menor! Tente novamente.")

    else:
        # Se o jogador não acertar em 4 tentativas, o jogo termina e mostra o número sorteado
        print(f"Você não acertou! O número sorteado era {numero_sorteado}.")
    
# Chama a função principal
main()
