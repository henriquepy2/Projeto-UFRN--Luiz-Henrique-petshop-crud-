#Projeto CRUD Pet Shop Luiz Henrique Souza Da Silva 
client = []
animal = []
nume = []
agend = []
#CRUD


resp = " "
while resp != "0":
   
    print("PET SHOP YOUR PET  🐱")
    print("SERVIÇOS DISPONIVEIS:🐶    🐾 ")
    print()
    print("1.Cadastrar Clientes")
    print("2.Listar Clientes ")
    print("3.Atualizar Clientes ")
    print("4.Excluir Clientes")
    print("5.Lista de serviços")
    print()
   
   
   
    print("6.INFORMAÇÕES ℹ️ ")
    print("0.Sair")
    print()
    print()

    resp = input("Escolha um desses trabalhos:  ")
   
    if resp == "1":
        #CREATE
        print("Muito bem você Escolheu para cadastrar clientes")
        print()
        cliente = input("Digite o seu nome:  ")
        pet = input("Digite o nome do seu pet:  ")
        num = int(input("Digite o seu número:  "))
        dia = int(input("Digite um dia de agendamento:  "))
       
        client.append(cliente)
        animal.append(pet)
        nume.append(num)
        agend.append(dia)
        print()
       
        print("Cliente cadastrado com Sucesso!!")
       
        print()
        input  ("Digite ENTER para continuar")
       
    elif resp == "2":
        #READ
        if len(client) == 0:
            print("Nenhum cliente Cadastrado!!ℹ️")
            print()
            input ("Digite Enter para Continuar")
           
        else:
            print(
                f"Cliente Cadastrado {client}\n"
                f"Nome do Animal {animal}\n"
                f"Telefone: {nume}\n"
                f"Agendado para o dia: {agend}")
           
               
            input("Digite enter para continuar")
       
    elif resp == "3":
        #UPTADE
        if len(client) == 0:
            print("Nenhum Cliente Cadastrado")
            print()
            input("Digite Enter para continuar")
           
        else:
            for i, nome in enumerate(client):
                print(i, nome)
                perg = int(input("Qual indice voce deseja Atualizar: "))
               
                if 0 <= perg < len(client):
                    valor_novo = str(input("Digite um novo nome:  "))
                    client[perg] = valor_novo
                   
                    print("Cliente Atualizado Com Sucesso!!")
                    print()
                   
                input("Digite Enter para Continuar")
       
       
    elif resp == "4":
        #DELETE
        if len(client) == 0:
            print("No momento não Existe Nenhum Cliente Cadastrado")
           
            input("Digite ENTER para continuar")
           
        else:
            for i, cliente in enumerate(client):
                print(i, cliente)
               
           
            perg = int(input("Quem Você Deseja excluir:  "))
           
            if 0 <= perg < len(client):
                client.pop(perg)
                animal.pop(perg)
                nume.pop(perg)
                agend.pop(perg)
               
                print("Cliente Removido com Sucesso!!")
               
            else:
                print("Inválido")
               
            input("Digite Enter Para continuar")
           
               
       
    elif resp == "5":
        print("PET SHOP YOUR PET  🐱")
        print("SERVIÇOS DISPONIVEIS:🐶    🐾 ")
        print()
        print("1.Banho --- R$ 50,00🛀 ")
        print("2.Tosa --- R$ 70,00🐩 ")
        print("3.Banho e Tosa --- R$ --- R$ 120,00 🛁  🐈")
        print("4.Corte de Unhas --- R$ 25,00🐾")
        print("5.Limpeza de Ouvidos --- R$ 30,00")
       
        input("Digite Enter Para Continuar")
           
           
       
   
   
       
    elif resp == "6":
        #INFORMAÇÕES
        print("Esse código foi produzido por:")
        print("LUIZ HENRIQUE SOUZA DA SILVA")
        print("do curso de BSI-UFRN 2026.1")
        print("no dia 28/05/2026.")
        print()
        print()
        input ("TECLE ENTER PARA CONTINUAR")
       
   
       
print("fim de programa")