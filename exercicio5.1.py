from dataclasses import dataclass

@dataclass
class Cliente:
    Nome: str
    Email: str
    Celular: str
    
    lista = []
    
    def criar_cliente():
        Nome = input("Digite seu Nome: ")
        Email = input("Digite seu Email: ")
        Celular = input("Digite seu número: ")
        Cliente_digitado = Cliente(nome,email,celular)
        lista.append(cliente_digitado)
        print("Cliente cadastrado com sucesso. ")
        
        def menu():
            print("1- Agendamento: ")
            print("2- reagendamento: ")
            print("3- Cancelamento: ")
            return input("\n Digite a opção: ")
            
        while True:
            opcao = menu()
            if opcao =="1":
                criar_agendamento()
            
            elif opcao =="2":
                criar_reagendamento()
                
            elif opcao =="3":
                criar_cancelamento()
            
        
        def menu():
            print("1- Corte simples:")
            print("2- Corte + Barba: ")
            print("3- Barba completa: ")
            print("4- Corte social: ")