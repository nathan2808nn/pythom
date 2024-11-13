import random

# Função para exibir as opções de escolha
def mostrar_opcoes():
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

# Função para determinar o vencedor
def determinar_vencedor(usuario, computador):
    if usuario == computador:
        return "Empate!"
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "papel" and computador == "pedra") or \
         (usuario == "tesoura" and computador == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

# Dicionário para mapear as escolhas numéricas para as opções
opcoes = {1: "pedra", 2: "papel", 3: "tesoura"}

# Início do jogo
print("Bem-vindo ao jogo JoKenPo (Pedra-Papel-Tesoura)!")
mostrar_opcoes()

# Lê a escolha do usuário
try:
    escolha_usuario = int(input("Digite o número correspondente à sua escolha: "))
    if escolha_usuario not in opcoes:
        print("Escolha inválida! Tente novamente.")
    else:
        escolha_usuario = opcoes[escolha_usuario]
        print(f"Você escolheu: {escolha_usuario.capitalize()}")

        # O computador faz sua escolha aleatória
        escolha_computador = random.choice(["pedra", "papel", "tesoura"])
        print(f"O computador escolheu: {escolha_computador.capitalize()}")

        # Determina o vencedor
        resultado = determinar_vencedor(escolha_usuario, escolha_computador)
        print(resultado)

except ValueError:
    print("Por favor, digite um número válido (1, 2 ou 3).")
