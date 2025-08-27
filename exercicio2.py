Exercicio 2- Codigo e diagrama 


def menu():
    print("\n--- Sisterma de cadastro de pacientes---")
    print("1 - Cadastrar Paciente ")
    print("2 - Mostrar paciente cadastrado")
    print("3 - Atender Paciente")
    print("0 - Sair")
    return input ("Escolha a opção: ")
    
    #Variaveis de controle
Lista_de_nomes = []
quantidade = 0

opcao = menu()
if opcao == "1":
    paciente =input("Digite o nome do paciente: ")
    quantidade =0
    print(f"Paciente '{paciente}' cadastrado com sucesso!")
    Lista_de_nomes.insert(0,paciente)


    