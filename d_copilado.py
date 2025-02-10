def alterar_cliente():
    if not os.path.exists("clientes.csv"):
        print("Nenhum cadastro encontrado.")
        return

    while True:
        codigo_digitado = input("Digite o código do cliente que deseja alterar: ")

        if codigo_digitado.isdigit():
            
            dados = abrir_arquivo_r("clientes.csv")

            # None - definido que não foi encontrado nome, tipo uma lista_vazia mas não é uma lista
            linha_encontrada = None
            # for - pra cada linha, na coluna não definida ainda
            # enumerate - gera índice pegando os dados da 2º linha, enumerando começando de 1
            for linha, coluna in enumerate(dados[1:], start=1):
                # se (definindo coluna 0) que é a primeira, estiver o código
                if coluna[0] == codigo_digitado:
                    # manda pra variável a linha encontrada e segue
                    linha_encontrada = linha
                    break
                
            if linha_encontrada is None:
                print("Nenhum cadastro encontrado.")
                return
            
            novo_nome = input("Digite o novo nome para o cliente: ").strip()
            if not novo_nome:
                print("Nenhum nome foi informado. Voltando ao menu principal.")
                return
            
            nova_idade = input("Digite a nova idade para o cliente: ")
            if not nova_idade.isdigit():
                print("Nenhuma idade foi informado. Voltando ao menu principal.")
                return
            
            novo_telefone = input("Digite o novo telefone para o cliente: ")
            if not len(novo_telefone) == 11 and novo_telefone.isdigit():
                print('O telefone deve ter 11 dígitos (DDD + números). Ex.99999999999.')
                return
            novo_telefone_formatado = f"({novo_telefone[:2]}) {novo_telefone[2:7]}-{novo_telefone[7:]}"
            
            # atualiza o dado na matriz
            # dados[nome] - foi determinado anteriormente quando encontramos o nome na linha
            # [1] - refere-se à 2° coluna e pega o novo nome e coloca no lugar
            dados[linha_encontrada][1] = novo_nome
            dados[linha_encontrada][2] = nova_idade
            dados[linha_encontrada][3] = novo_telefone_formatado

            # reescreve o arquivo com os dados atualizados
            with open("clientes.csv", "w", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows(dados)
            print("Dados do cliente alterados com sucesso.")
            break
        else:
            print("O código do cliente deve conter apenas números.")   

def abrir_arquivo_r(nome_arquivo):
    with open(nome_arquivo, "r", newline="") as arquivo:
        conversor = csv.reader(arquivo)
        dados = list(conversor)
    return dados
