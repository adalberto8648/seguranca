import random
import string
import hashlib
import os
import re

def acessar_projeto():

    print("\n-------------------------------")
    print("|           PROJETO           |")
    print("-------------------------------\n")

    nome = "senha"
    senha = "123"
    
    while True:
        acesso_nome = input("Digite o nome: ")
        if acesso_nome == nome:
            break
        print("Nome inválido, digite novamente.")

    while True:
        acesso_senha = input("Digite a senha: ")
        if acesso_senha == senha:
            print("Acesso permitido.")
            break
        print("Senha inválida, digite novamente.")

    while True:
        print("\n----- Menu PROJETO -----")
        print("1 - Clientes")
        print("2 - Fornecedor")
        print("3 - Produtos")
        escolha = input("\nEscolha uma das opções: ")
        print("-" * 24 + "\n")
        
        if escolha == "1":
            clientes.menu_clientes()
        elif escolha == "2":
            fornecedores.menu_fornecedores()
        elif escolha == "3":
            produtos.menu_produtos()
        else:
            print("Opção inválida, tente novamente\n")

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

    salt = os.urandom(16).hex()
    print(f"Salt gerado: {salt}")
    hash_senha = gerar_hash(senha_usuario + salt)

    print(f"Hash SHA-256 da senha: {hash_senha}")
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
        if not senha_usuario:
            print("Nenhuma senha informada. Tente novamente.")
        else:
            return senha_usuario

def validar_senha(senha_cadastra_ou_alterar):
    if len(senha_cadastra_ou_alterar) < 8:
        print("A senha precisa ter pelo menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", senha_cadastra_ou_alterar):
        print("A senha precisa ter pelo menos uma letra maiúscula.")
        return False
    if not re.search(r"[a-z]", senha_cadastra_ou_alterar):
        print("A senha precisa ter pelo menos uma letra minúscula.")
        return False
    if not re.search(r"\d", senha_cadastra_ou_alterar):
        print("A senha precisa ter pelo menos um número.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha_cadastra_ou_alterar):
        print("A senha precisa ter pelo menos um caractere especial.")
        return False
    return True

def gerar_hash(salt_cadastro_ou_alterar):
    sha256 = hashlib.sha256()
    sha256.update(salt_cadastro_ou_alterar.encode('utf-8'))
    return sha256.hexdigest()

def salvar_senha(nome, salt, hash_senha):
    with open("config.sys", "a") as arquivo:
        arquivo.write(f"{nome}:{salt}:{hash_senha}\n")
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
            nova_senha_usuario = senha_digitada()
            
            print("----------------------------------")

            print(f"Nova senha cadastrada pelo usuário: {nova_senha_usuario}")

            while not validar_senha(nova_senha_usuario):
                print("Senha inválida. Tente novamente.")
                nova_senha_usuario = senha_digitada()

            novo_salt = os.urandom(16).hex()
            print(f"Novo salt gerado: {novo_salt}")
            novo_hash_senha = gerar_hash(nova_senha_usuario + novo_salt)

            print(f"Hash SHA-256 da nova senha: {novo_hash_senha}")
            print("----------------------------------\n")

            novas_linhas.append(f"{nome_usuario}:{novo_salt}:{novo_hash_senha}\n")
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