import random
import string
import hashlib

def tamanho_senha():
    while True:
        try:
            print("----------------------------------")
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
    print("----------------------------------")
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

def gerar_hash(senha_gerada):
    sha256 = hashlib.sha256()
    sha256.update(senha_gerada.encode('utf-8'))
    return sha256.hexdigest()

tamanho = tamanho_senha()
caracteres = escolha()
senha_gerada = ''.join(random.choice(caracteres) for numero in range(tamanho))
senha_hash = gerar_hash(senha_gerada)

print("----------------------------------")
print(f"Senha {senha_gerada} gerada com sucesso:")
print(f"Hash SHA-256 da senha: {senha_hash}")
print("----------------------------------\n")