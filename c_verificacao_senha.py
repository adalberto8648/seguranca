import random
import string
import hashlib
import os
import re

def acessar_projeto():

    print("\n---------------------------------")
    print("|CADASTRO DE SENHA CRIPTOGRAFADO|")
    print("---------------------------------")

    while True:
        print("----- Menu PROJETO -----")
        print("1 - Cadastrar")
        print("2 - Sair")
        escolha = input("\nEscolha uma das opções: ")
        print("-" * 24 + "\n")
        
        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
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
    with open("senhas.txt", "a") as arquivo:
        arquivo.write(f"{nome}:{salt.hex()}:{hash_senha}\n")
    print("Senha armazenada com sucesso!\n")

acessar_projeto()