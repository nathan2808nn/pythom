# Lê o ano de nascimento do rapaz
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Obtém o ano atual
from datetime import datetime
ano_atual = datetime.now().year

# Calcula a idade do rapaz
idade = ano_atual - ano_nascimento

# Verifica a situação do alistamento
if idade < 18:
    faltam_anos = 18 - idade
    print(f"Ainda faltam {faltam_anos} anos para o seu alistamento militar.")
elif idade == 18:
    print("Você deve se alistar este ano.")
else:
    anos_passados = idade - 18
    print(f"Você já deveria ter se alistado há {anos_passados} anos.")
