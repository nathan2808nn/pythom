# Lê o ano de nascimento da pessoa
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Obtém o ano atual
from datetime import datetime
ano_atual = datetime.now().year

# Calcula a idade
idade = ano_atual - ano_nascimento

# Verifica se a pessoa pode votar
if idade >= 16:
    print(f"Você tem {idade} anos. Você pode votar!")
else:
    print(f"Você tem {idade} anos. Você não pode votar.")
