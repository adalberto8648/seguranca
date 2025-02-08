import random
import string

def tamanho_senha():
    while True:
        try:
            tamanho = int(input("Digite a quantidade de números da senha: "))
            if tamanho < 0:
                print("O tamanho da senha não pode ser negativo, ou digite 0 para sair.")
            elif tamanho == 0:
                print("VOCÊ NÃO GEROU SENHA. VOLTE SEMPRE.")
                exit()
            else:
                return tamanho
        except ValueError:
            print("O tamanho da senha não pode ser negativo, ou digite 0 para sair.")

def escolha():
    print("----------------------------------\n")
    print("Escolha o nível para geração da senha.\n")
    print("Nível 1 - Senha fraca (Letras)")
    print("Nível 2 - Senha média (Letras e Números)")
    print("Nível 3 - Senha forte (Letras, Números e Caracteres Especiais)")

    while True:
        try:
            caracteres_disponiveis = []
            escolha = int(input("\nDigite o nível escolhido: "))
            if escolha <= 0:
                print("Escolha entre as opçôes 1, 2 ou 3 par ao nível de senha:")
                continue
            elif escolha == 1:
                caracteres_disponiveis = string.ascii_letters
            elif escolha == 2:
                caracteres_disponiveis = string.ascii_letters + string.digits
            elif escolha == 3:
                caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation
            return caracteres_disponiveis
        except ValueError:
            print("Escolha entre as opçôes 1, 2 ou 3 par ao nível de senha:")

tamanho = tamanho_senha()
caracteres_disponiveis = escolha()

senha = ''.join(random.choice(caracteres_disponiveis) for _ in range(tamanho))

print("Senha gerada:", senha)

