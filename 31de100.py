import random


def mostrar_opcoes():
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")


def determinar_vencedor(usuario, computador):
    if usuario == computador:
        return "Empate!"
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "papel" and computador == "pedra") or \
         (usuario == "tesoura" and computador == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

opcoes = {1: "pedra", 2: "papel", 3: "tesoura"}


print("Bem-vindo ao jogo JoKenPo (Pedra-Papel-Tesoura)!")
mostrar_opcoes()


try:
    escolha_usuario = int(input("Digite o número correspondente à sua escolha: "))
    if escolha_usuario not in opcoes:
        print("Escolha inválida! Tente novamente.")
    else:
        escolha_usuario = opcoes[escolha_usuario]
        print(f"Você escolheu: {escolha_usuario.capitalize()}")

   
        escolha_computador = random.choice(["pedra", "papel", "tesoura"])
        print(f"O computador escolheu: {escolha_computador.capitalize()}")

        
        resultado = determinar_vencedor(escolha_usuario, escolha_computador)
        print(resultado)

except ValueError:
    print("Por favor, digite um número válido (1, 2 ou 3).")
