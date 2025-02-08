import random
import string

while True:
    try:
        tamanho = int(input("Digite a quantidade de números da senha: "))
        if tamanho < 0:
            print("O tamanho da senha não pode ser negativo, ou digite 0 para sair.")
        elif tamanho == 0:
            print("VOCÊ NÃO GEROU SENHA. VOLTE SEMPRE.")
            exit()
        else:
            break
    except ValueError:
        print("O tamanho da senha não pode ser negativo, ou digite 0 para sair.")
        
caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print("Senha gerada:", senha)