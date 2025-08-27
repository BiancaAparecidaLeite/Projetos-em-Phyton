#Exercicio 2

# Sistema de estoque com apenas 1 produto
# 1. Opção de cadastro do nome do produto.
# 2. Opção de retirar produto do estoque (precisa ver se tem o produto)
# 3. Opção de adicionar produto no estoque (precisa adicionar um numero maior que 0)
# 4. Opção de ver a quantidade no estoque


def menu():
    print("\n--- Sistema de Estoque---")
    print("1 - Cadastrar evento")
    print("2 - Retirar ingresso")
    print("3 - Adicionar ingresso")
    print("4 - Ver qualidade de ingresso")
    print("0 - Sair")
    return input (" Escolha a opção: ")
    
    #Variáveis de controle
produto = None
quantidade = 0
    
while True:
    opcao = menu()
        
    if opcao == "1":
        produto =input("Digite o nome do evento:")
        quantidade =0
        print(f"Produto '{produto}' cadastrado com sucesso!")
    elif opcao == "2":
        if produto is None:
            print("Nenhum evento cadastrado ainda!")
    else:
        retirar = int(imput("Digite a quantidade a retirar: "))
        if retirar <= 0:
            print("A quantidade deve ser maior que zero!")
        elif retirar > quantidade:
            print("Quantidade insuficiente em estoque!")
        else:
            quantidade -= retirar
        print(f"Retirado{retirar} unidade(s). ingressos atual:{quantidade}")
    
        elif opcao == "3":
        if produto is None:
            print("Nenhum ingresso cadastrado ainda!")
    else:
            adicionar = int(imput("Digite a quantidadea adicionar"))
        if adicionar <= 0:
            print("A quantidade deve ser maior que zero")
    else:
            quantidade += adicionar
            print(f"Adicionado {adicionar} unidade(s). Estoque atual: {quantidade}:")
            elif opcao == "3":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            adicionar = int(imput("Digite a quantidadea adicionar"))
        if adicionar <= 0:
            print("A quantidade deve ser maior que zero")
        else:
      quantidade += adicionar
      print(f"Adicionado {adicionar} unidade(s). Estoque  de ingressos atual: {quantidade}:")
                
    elif opcao == "4":
        if produto is None:
        print("Nenhum evento cadastrado ainda! ")
    else:
        print(f"Produto: {produto} | Quantidade de ingressos em estoque:{quantidade}")
                                       
    elif opcao == "0":
        print("Saindo do sistema...até mais!")
        break
                                                            
    else:
        print("Opção iválida! tente novamente.")
                