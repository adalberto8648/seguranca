import random
import string
import hashlib
import os
import re

def acessar_menu():

    print("\n---------------------------------")
    print("|CADASTRO DE SENHA CRIPTOGRAFADO|")
    print("---------------------------------")

    while True:
        print("----- Menu PROJETO -----")
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Sair")
        escolha = input("\nEscolha uma das opções: ")
        print("-" * 24 + "\n")
        
        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            alterar_senha()
        elif escolha == "3":
            print("VOCÊ NÃO ACESSOU. SAINDO -->\n")
            exit()
        else:
            print("Opção inválida, tente novamente\n")

def cadastrar_usuario():
    nome = nome_usuario()
    senha_digitada = senha_escolhida()

    while not validar_senha(senha_digitada):
        print("Senha inválida. Tente novamente.")
        senha_digitada = senha_escolhida()

    print("----------------------------------")
    print(f"Senha gerada: {senha_digitada}")

    caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation
    senha_gerada = ''.join(random.choice(caracteres_disponiveis) for numero in range(5))
    print(f"Senha gerada: {senha_gerada}")

    salt = os.urandom(16)
    print(f"Salt gerado: {salt.hex()}")
    senhas_com_salt_hex = senha_digitada + senha_gerada + salt.hex()
    hash_senha = gerar_hash(senhas_com_salt_hex)

    print(f"Hash SHA-256 da senha: {gerar_hash(senhas_com_salt_hex)}")
    print("----------------------------------\n")

    salvar_senha(nome, salt, hash_senha)

def nome_usuario():
    while True:
        print("----------------------------------")
        nome = input("Digite aqui o seu nome: ").strip()      

        if nome == "0":
            print("VOCÊ NÃO DIGITOU A SENHA. SAINDO -->")
            exit()
        else:
            return nome

def senha_escolhida():
    while True:
        print("----------------------------------")
        senha_digitada = input("Digite aqui a sua senha: ").strip()      

        if senha_digitada == "0":
            print("VOCÊ NÃO DIGITOU A SENHA. SAINDO -->")
            exit()
        else:
            return senha_digitada

def validar_senha(senha_digitada):
    if len(senha_digitada) < 8:
        print("A senha precisa ter pelo menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", senha_digitada):
        print("A senha precisa ter pelo menos uma letra maiúscula.")
        return False
    if not re.search(r"[a-z]", senha_digitada):
        print("A senha precisa ter pelo menos uma letra minúscula.")
        return False
    if not re.search(r"\d", senha_digitada):
        print("A senha precisa ter pelo menos um número.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha_digitada):
        print("A senha precisa ter pelo menos um caractere especial.")
        return False
    return True

def gerar_hash(senhas_com_salt_hex):
    sha256 = hashlib.sha256()
    sha256.update(senhas_com_salt_hex.encode('utf-8'))
    return sha256.hexdigest()

def salvar_senha(nome, salt, hash_senha):
    with open("config.sys", "a") as arquivo:
        arquivo.write(f"{nome}:{salt.hex()}:{hash_senha}\n")
    print("Senha armazenada com sucesso!\n")

def alterar_senha():
    if not os.path.exists("config.sys"):
        print("Nenhum cadastro encontrado.")
        return

    nome_usuario = input("Digite o nome do usuário para alterar a senha: ").strip()

    with open("config.sys", "r") as arquivo:
        linhas = arquivo.readlines()
    
    usuario_encontrado = False
    novas_linhas = []

    for linha in linhas:
        partes = linha.strip().split(":")
        if partes[0] == nome_usuario:
            nova_senha = input("Digite a nova senha: ").strip()
            if not nova_senha:
                print("Nenhuam senha informada. Voltando ao menu.")
                return
            
            print("----------------------------------")

            print(f"Senha gerada: {nova_senha}")

            novos_caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation
            nova_senha_gerada = ''.join(random.choice(novos_caracteres_disponiveis) for numero in range(5))
            print(f"Senha gerada: {nova_senha_gerada}")

            novo_salt = os.urandom(16).hex()
            novo_hash = hashlib.sha256((nova_senha + nova_senha_gerada + novo_salt).encode()).hexdigest()

            novas_linhas.append(f"{nome_usuario}:{novo_salt}:{novo_hash}\n")
            usuario_encontrado = True
        else:
            novas_linhas.append(linha)

    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return
        
    with open("config.sys", "w") as arquivo:
        arquivo.writelines(novas_linhas)

    print("Senha alterada com sucesso.") 

acessar_menu()