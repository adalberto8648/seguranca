#import random
#import string
#caracteres = string.ascii_letters + string.digits
#tamanho = int(input("Digite o tamanho da senha: "))
#senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
#print("Senha gerada:", senha)

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
tamanho = tamanho_senha()

def escolha():
    print("----------------------------------\n")
    print("Escolha o nível para geração da senha.\n")
    print("Nível 1 - Senha fraca (Letras)")
    print("Nível 2 - Senha média (Letras e Números)")
    print("Nível 3 - Senha forte (Letras, Números e Caracteres Especiais)")

    while True:
        try:
            caracteres_disponiveis = []
            escolha = int(input("\nDigite o nível de dificultade da senha: "))
            if escolha <= 0 or escolha > 3:
                print("Escolha entre as opções 1, 2 ou 3 par ao nível de senha:")
                continue
            elif escolha == 1:
                caracteres_disponiveis = string.ascii_letters
            elif escolha == 2:
                caracteres_disponiveis = string.ascii_letters + string.digits
            elif escolha == 3:
                caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation
            return caracteres_disponiveis
        except ValueError:
            print("Escolha entre as opções 1, 2 ou 3 par ao nível de senha:")
caracteres = escolha()

def geracao_senha():
    #''.join vai servir pra unir os números do random.choice que está vindo do
    #se '-'.join vai colocar esse espaço entre os números
    #caracteres escolhido e roda no loop for o range de numero determinado no tamanho
    senha_gerada = ''.join(random.choice(caracteres) for numero in range(tamanho))
    return senha_gerada
senha_gerada = geracao_senha()

print("----------------------------------")
print(f"Senha {senha_gerada} gerada com sucesso:")
print("----------------------------------\n")