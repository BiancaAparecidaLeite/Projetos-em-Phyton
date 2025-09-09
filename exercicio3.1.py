from dataclasses import dataclass
from datetime import datetime
# é uma classe de publicação

@dataclass
class Publicacao:
    conteudo: str
    descricao:str
    autor:str
    data_hora: datetime
    curtidas: int = 0
    
    lista_publicacoes = []
    #Aqui estamos criando a função de publicações.
    def criar_publicacoes():
        print("\n== CRIAR PUBLICAÇÃo === ")
        conteudo = input("Digite o conteudo da publicação: ")
        descricao = input("Digite a descrição: ")
        autor = input("Digite o nome do autor: ")
        data_hora = timeline.now()
        
        nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
        lista_publicacoes.append(nova_publicacao)
        print("Publicação criada com sucesso!")
        
    def curtir_publicacao():
        print("\n=== CURTIR PUBLICAÇÃO ===")
        if not lista_publicacoes:
            print(" Nenhuma publicação disponível.")
            return
        
        #aqui nos estamos criando a função de visualizar o feed.    
        visualizar_feed()
        try:
            indice = int(input("Digite o número da publicação para curtir: ")) -1
            if 0 <= indice < len (lista_publicacoes):
                lista_publicacoes[indice].curtidas+= 1
                print("Publicação curtida!")
            else:
                print("Publicação não encontrada. ")
        except ValueError:
            print("Número inválido.") 
    #aqui criamos uma função na qual se você não tiver publicações irá aparecer uma mensangem falando que você não tem publicação.
    def visualizar_feed():
        print("\n=== FEED ===")
        if not lista_publicacoes:
            print("Nenhuma publicação disponivel.")
            return
        
        for i, pub in enumerate(lista_publicacoes,1):
            print(f"{i}. {pub.autor} - {pub.curtidas} curtidas ")
            print(f"  {pub.conteudo[:50]} ...")
            print(f"  {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
            print ("-" * 40)
            
    def visualizar_publicacao_individual():
        print("\n=== VISUALIZAR PUBLICAÇÃO ===")
        if not lista_publicacoes:
            print("Nenhuma publicação disponível.")
            return
     # estamos criando uma função para você visualizar o feed   
        visualizar_feed()
        try:
            indice = int(input("Digite o número da publicação: ")) -1
            if 0 <= indice < len(lista_publicacoes):
                pub = lista_publicacoes[indice]
                print(f"\nAutor: {pub.autor}")
                print(f"Data: {pub.data_hora.strtime('%d/%m/%Y %H:%M')}")
                print(f"Conteúdo: {pub.conteudo}")
                print(f"Descrição: {pub.descricao}")
                print(f"Curtidas: {pub.curtidas}")
            else:
                #se a função nao for encontrada ele exibirá a mensagem a baixo.
                print("Publicação não encontrada.")
        except VaLueerror: 
            print:("Número inválido.")
            
    def visualizar_publicacoes_por_autor():
        print("\n===PUBLICAÇÕES POR AUTOR ===")
        if not lista_publicacoes:
            print("Nenhuma publicação disponivel.")
            return
        
        autor = input("Digite o nome do autor:")
        publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower()] 
        
        if not publicacoes_autor:
            print(f"Nenhuma publicação encontrada para {autor}.")
            return
        
        print(f"\nPublicacoes de {autor}:")
        for pub in publicacoes_autor:
            print(f" - {pub.conteudo[:50]}...({pub.curtidas} curtidas")
            print(f" {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
            print("-" * 30)
            
            
    def menu():
        #enquanto for verdade ele vai seguir essa lista
        while True:
            print("\n=== REDE SOCIAL===")
            print("1. Criar Publicação")
            print("2. Curtir Publicação")
            print("3. Visualizar Feed")
            print("4. Visualizar publicação individual")
            print("5. Visualizar publicação por Autor")
            print("0. Sair")
            
            opcao = input ("Escolha uma opção: ")
            
            if opcao == "1":
                criar_publicacao()
            elif opcao == "2":
                curtir_publicacao()
            elif opcao == "3":
                visualizar_feed()
            elif opcao == "4":
                visualizar_publicacao_individual()
            elif opcao == "5":
                visualizar_publicacao_por_autor()
            elif opcao == "0":
                print("Saindo...")
                break 
        else:
            print("Opçãp inválida!")
            
    if __name__ == "__main__":
        menu()
            

            
        
        
            
            
        
    
   