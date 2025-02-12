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
    senha_usuario = senha_digitada()

    while not validar_senha(senha_usuario):
        print("Senha inválida. Tente novamente.")
        senha_usuario = senha_digitada()

    print("----------------------------------")
    print(f"Senha cadastrada pelo usuário: {senha_usuario}")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_random = ''.join(random.choice(caracteres) for numero in range(5))
    print(f"5 dígitos gerados por random: {senha_random}")

    salt = os.urandom(16)
    print(f"Salt gerado: {salt.hex()}")
    senhas_com_salt = senha_usuario + senha_random + salt.hex()
    hash_senha = gerar_hash(senhas_com_salt)

    print(f"Hash SHA-256 da senha: {gerar_hash(senhas_com_salt)}")
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

def senha_digitada():
    while True:
        print("----------------------------------")
        senha_usuario = input("Digite aqui a sua senha ou 0 pra sair: ").strip()      

        if senha_usuario == "0":
            print("VOCÊ NÃO DIGITOU A SENHA. SAINDO -->")
            exit()
        else:
            return senha_usuario

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

def nova_senha_digitada():
    while True:
        nova_senha_usuario = input("Digite a nova senha ou 0 pra sair: ").strip()

        if nova_senha_usuario == "0":
            print("VOCÊ NÃO DIGITOU A SENHA. SAINDO -->")
            exit()
        if not nova_senha_usuario:
            print("Nenhuma senha informada. Tente novamente.")
        else:
            return nova_senha_usuario

def validar_nova_senha(nova_senha_digitada):
    if len(nova_senha_digitada) < 8:
        print("A senha precisa ter pelo menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", nova_senha_digitada):
        print("A senha precisa ter pelo menos uma letra maiúscula.")
        return False
    if not re.search(r"[a-z]", nova_senha_digitada):
        print("A senha precisa ter pelo menos uma letra minúscula.")
        return False
    if not re.search(r"\d", nova_senha_digitada):
        print("A senha precisa ter pelo menos um número.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", nova_senha_digitada):
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
            nova_senha_usuario = nova_senha_digitada()
            
            print("----------------------------------")

            print(f"Nova senha digitada: {nova_senha_usuario}")

            while not validar_nova_senha(nova_senha_usuario):
                print("Senha inválida. Tente novamente.")
                nova_senha_usuario = nova_senha_digitada()

            novos_caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation
            nova_senha_gerada = ''.join(random.choice(novos_caracteres_disponiveis) for numero in range(5))
            print(f"Senha alterada: {nova_senha_gerada}")

            novo_salt = os.urandom(16).hex()
            novo_hash = hashlib.sha256((nova_senha_usuario + nova_senha_gerada + novo_salt).encode()).hexdigest()

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