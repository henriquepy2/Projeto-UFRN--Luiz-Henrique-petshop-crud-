#ATUALIZAÇOS O CODIGO FOI MODULARIZADO COM FUNÇOES DEF E AGORA COM COM IDDS NOS ESTOQUE E NO SERVIÇO
#DIA 26/06 SERA MUDADO O AGENDAMENTO E COLOCADO OS RELATORIOS
#CODIGO MUDADO DIA 24/06


#PROJETO PETSHOP




import os 
import pickle

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
        
    else:
        os.system("clear")
        
        
        
def recupera_clientes():
    try:
        arq = open("clientes.dat", "rb")
        clientes = pickle.load(arq)
        arq.close()
    except:
        clientes = {
            "001": ["João de Souza", "99597155", "Tob"],
            "002": ["Maria Betania", "99875541", "Bela"],
            "003": ["Chris", "40028922", "Fred"]
        }
    return clientes
# ANIMAIS
def recupera_animais():
    try:
        arq = open("anim.dat", "rb")
        animais = pickle.load(arq)
        arq.close()
    except:
        animais = {
            "001": ["Tob", "28 de Abril"],
            "002": ["Bela", "10 de Abril"],
            "003": ["Fred", "20 de Abril"]
        }
    return animais
    
    #FUNÇÃO PARA GRAVA OS clientes
    
    
def grava_clientes(clientes):
    arq = open("clientes.dat", "wb")
    pickle.dump(clientes, arq)
    arq.close()
    
    #GRAVAR CLIENTES



def grava_animais(anim):
    arq = open("anim.dat", "wb")
    pickle.dump(anim, arq)
    arq.close()
    
    
    #GRAVAR ANIMAIS
    
clientes= {
   "001": ["João de Souza", "99597155", "Tob"],
    "002": ["Maria Betania", "99875541", "Bela"],
   "003": ["Chris", "40028922", "Fred"]
}
servicos = {
    "001": ["1.Tosa"], 
    "002": ["Banho e Tosa"],
    "003": ["3.Corte De Unhas"],
    "004": ["4.Limpeza De ouvidos"]

}


agenda = [ "1.Dia 13 de julho", "2.Dia 15 de julho ", "3.Dia 12 de Julho"]




estoque = {
    "001": ["1.Ração Royal Canin "], 
    "002": ["2.Shampoo"],
    "003": ["3.Petiscos"],
    "004": ["4.Coleiras"]
}

anim = {
    "001": ["Tob", "28 de Abril"],
    "002": ["bela", "10 de Abril"],
    "003": ["fred", "20 de Abril"]
}

while True:
    
    print("\t\t\tPrograma Pet shop\t\t\t")
    print()

    print("\t\t\t1.Módulo Clientes\t\t\t")
    print("\t\t\t2.Módulo Serviços\t\t\t")
    print("\t\t\t3.Módulo Agendamentos\t\t\t")
    print("\t\t\t4.Módulo De Estoque\t\t\t")
    print("\t\t\t5. Módulo de Vacina\t\t\t")
    print()
    print("\t\t\t6. Informações\t\t\t")
    
    print()
    print()
    print("\t\t\t0.Sair\t\t\t")
    
    
    print()
    print()
    print("\t\t\t6. INFORMAÇÕES\t\t\t")

    perg = str(input("Digite um Serviço para Escolher: "))
    
    
                 #MODULO CLIENTES
    if perg == "1":
        limpar_tela()
        while True:
            print("\t\tMódulo Clientes\t\t")
            print()
            print("\t\t1.Cadastrar Clientes\t\t")
            print("\t\t2.Listar Clientes\t\t")
            print("\t\t3.Atualizar Clientes\t\t")
            print("\t\t4.Excluir Clientes\t\t")
            print("\t\t0.SAIR\t\t")
            perg1 = str(input("Digite um serviço para Escolher: "))
    
            if perg1 == "1":
                limpar_tela()
                idd = str(input("Digite o ID: "))
                nome = input("Digite o seu nome: ")
                num = str(input("Digite o seu número: "))
                pet = input("Digite o nome do seu pet: ")
                
                clientes[idd] = [nome, num,pet]
                
                print()
                print("Cliente Cadastrado Com Sucesso!")
                
                input("Digite Qualquer Tecla Para continuar")
        
        
        
    
    
            elif perg1 == "2":
                limpar_tela()
                dig = str(input("Digite a ID do cliente: "))
                if dig in clientes:
                    print(clientes[dig])
                    
                
                else:
                    print("Cliente Não Encontrado")
            
            
            elif perg1 == "3":
                limpar_tela()
                id_cliente = input("Digite o ID do cliente: ")
                
                
                if id_cliente in clientes:
                    nome = input("Digite Seu Nome: ")
                    num = input("Digite O seu Telefone: ")
                    pet = input("Digite o nome Do Seu pet: ")
                    
                    clientes[id_cliente][0] = nome
                    clientes[id_cliente][1] = num
                    clientes[id_cliente][2] = pet
                    
                    print("Cliente Atualizado Com Sucesso!!")
                    
                
                else:
                    print("Cliente Não Encontrado")

                    
                    
                    
                    
                    
            elif perg1 == "4":
                limpar_tela()
                for cliente in clientes:
                    print(cliente, clientes[cliente])
                    
                excluir = input("De Acordo Com o ID \n Quem Você Deseja Excluir: ")
                
                if excluir in clientes:
                    clientes.pop(excluir)
                    print("Cliente Excluído!!")
                    
                else:
                    print("Cliente Não Encontrado")
                    
                    
                    
            elif perg1 == "0":
                break
                
                
                #MODULO SERVIÇOS 
    elif perg == "2":
        
        limpar_tela()
       
        while True:
            print("\t\t\t2.Módulo Serviços\t\t\t")
            print()
            print("\t\t1.Cadastrar Serviços\t\t")
            print("\t\t2.Listar Serviços\t\t")
            print("\t\t3.Atualizar Serviços\t\t")
            print("\t\t4.Excluir Serviços\t\t")
            print("\t\t0.SAIR\t\t")
        
            perg3 = str(input("Digite Um Serviço Para Escolher: "))
        
            if perg3 == "1":
                serv = input("Qual Novo Serviço Você Quer colocar: ")
                serv1 = str(input("Digite o ID do Serviço:  "))
            
                servicos[serv1] = [serv]
            
            elif perg3 == "2":
                idd = str(input("Digite o ID do serviço:  "))
                if idd in servicos:
                    print(servicos[idd])
                print()
                input ("Digite Qualquer Tecla Para Continuar: ")
        
            elif perg3 == "3":
                print("Serviços cadastrados:")
                for codigo in servicos:
                    print(codigo, servicos[codigo][0])

                id_servico = input("Digite o ID do serviço que deseja atualizar: ")

                if id_servico in servicos:
                    novo_servico = input("Digite o novo nome do serviço: ")
                    servicos[id_servico][0] = novo_servico

                    print("Serviço atualizado com sucesso!")
                
                else:
                    print("Serviço não encontrado.")

                
                
            
                input ("Digite Qualque Tecla Para Continuar: ")
            
            elif perg3 == "4":
                for idd in servicos:
                    print(idd, servicos[idd][0])
                idd = str(input("Digite o ID do serviço que Você quer Excluir: "))
                
                if idd in servicos:
                    servicos.pop(idd)
                    print("Serviço Excluido Com Sucesso!!")
                    
                else:
                    print("Serviço não encontrado. ")
                    
                    
                    input ("Digite Qualque Tecla Para Continuar: ")
                
            
                
            if perg3 == "0":
                break
                
                
        # MODULO DE AGENDAMENTOS
    elif perg == "3":
        limpar_tela()
        while True: 
            print(" \t\t\t3.Módulo de Agendamentos\t\t\t")
            print()
            print("\t\t1.Adicionar Agendamento \t\t")
            print("\t\t2.Listar Agendamentos\t\t")
            print("\t\t3.Atualizar Agendamento\t\t")
            print("\t\t4.Excluir Agendamento\t\t")
            print("\t\t0.SAIR\t\t")
            perg = str(input("Escolha Um Desses Serviços: "))
        
            if perg == "1":
                for dia in agenda:
                    print(dia)
                    print()
                print("Dias ja escolhidos")
                
                print()
                dia = str(input("Escolha um Dia para que possamos Lhe atender: "))
                agenda.append(dia)  
            
                print()
                input("Digite Qualquer Tecla Para Continuar: ")
            
            elif perg == "2":
                print("Dias Listados De Trabalho")
                for dia in agenda:
                    print(dia)
                
                print()
                input ("Digite Qualquer Tecla Para Continuar: ")
            
        
            elif perg == "3":
                limpar_tela()
                for dia in agenda:
                    print(dia)
                
                perg = str(input("Digite um que Você Deseja Atualizar De acordo com a numeração dele: "))
            
                if perg == "1":
                    limpar_tela()
                    dia = str(input("Digite Qual Dia Desse mês Você Deseja ser atendido: "))
                    agenda[0] = dia
                    print()
                    print("Atualização Feita!!")
            
                elif perg == "2":
                    limpar_tela()
                    dia = str(input("Digite Qual Dia Desse mês Você Deseja ser atendido: "))
                    agenda[1] = dia
                    print()
                    print("Atualização Feita!!")
            
                elif perg == "3":
                    limpar_tela()
                    dia = str(input("Digite Qual Dia Desse mês Você Deseja ser atendido: "))
                    agenda[2] = dia
                    print()
                    print("Atualização Feita!!")
                
                input ("Digite Qualquer Tecla para Continuar")
            
            
            elif perg == "4":
                limpar_tela()
                for dia in agenda:
                    print(dia)
                
                print()
                print("Qual Dia Você Deseja Excluir")
                d = str(input("DIA(1 a 3) : "))
            
                if d == "1":
                    print("Você Excluiu o dia 13 de julho")
                    agenda.pop(0)
                
                elif d == "2":
                    print("Você excluiu o dia 15 de julho")
                    agenda.pop(1)
                
                elif d == "3":
                    print("Você excluiu o dia 12 de julho")
                    agenda.pop(2)
                
                input ("Digite Qualquer Tecla para Continuar")
            
            if perg == "0":
                break
        
    # MODULO DE ESTOQUE
    elif perg == "4":
        limpar_tela()
        while True:
            print(" \t\t\t4.Módulo de Estoque\t\t\t")
            print()
            print("\t\t1.Adicionar Item ao Estoque \t\t")
            print("\t\t2.Listar Estoque\t\t")
            print("\t\t3.Atualizar Item Do Estoque\t\t")
            print("\t\t4.Excluir Item Do Estoque\t\t")
            print("\t\t0.SAIR\t\t")
            
            perg = str(input("Escolhe Um Desses Serviços: "))
            
            if perg == "1":
                for idd in estoque:
                    print(idd, estoque[idd][0])
                    
                add = str(input("Digite um Item Para Ser Adicionado: "))
                idd = str(input("Digite o ID do Serviço:  "))
                
                estoque[idd] = [add]
                
                print("Item Adicionado Com Sucesso!!")
                
                input ("Digite Qualquer Tecla Para Continuar: ")
                
                
            elif perg == "2":
                idd = str(input("Digite o ID do Item:  "))
                if idd in estoque:
                    print(estoque[idd])
                    print()
                    print("Itens do Estoque")
                    
                    input ("Digite Qualquer Tecla Para Continuar: ")
                    
                    
            
            elif perg == "3":
                print("Itens cadastrados:")

                for idd in estoque:
                    print(idd, estoque[idd][0])

                it = input("Digite o ID do item que deseja atualizar: ")

                if it in estoque:
                    novo_item = input("Digite o nome do novo item: ")

                    estoque[it][0] = novo_item

                    print("Item atualizado com sucesso!")
                else:
                    print("Item não encontrado.")

                input("Digite qualquer tecla para continuar")
                
                
                
            
            elif perg == "4":
                for idd in estoque:
                    print(estoque[idd][0])
                    
                perg = str(input("Qual item Você deseja Apagar De acordo Com ID: "))
                
                if perg in estoque:
                    estoque.pop(perg)
                    print("Item excluído com sucesso!")
                else:
                    print("Item não encontrado.")

                input("Digite qualquer tecla para continuar")
                
            elif perg == "0":
                break
            
            
            
        #MODULO DE VACINAÇAO
    elif perg == "5":
        limpar_tela()
        while True:
            print(" \t\t\t5. Módulo de Vacinação\t\t\t")
            print()
            print("\t\t1. Registrar Vacinação\t\t")
            print("\t\t2. Listar Animais Vacinados\t\t")
            print("\t\t3. Atualizar Animais Vacinados\t\t")
            print("\t\t4. Excluir Animais Vacinados\t\t")
            print()
            print("\t\t0. SAIR\t\t")
            
            perg = str(input("Escolha Um Desses Serviços: "))
            
            if perg == "1":
                print("\t\t\tMuito Bem Você Escolheu Registrar a Vacinação\t\t\t")
                print()
                idd = str(input("Digite o ID do seu Animal: "))
                nome = str(input("Digite o nome do Seu animal: "))
                dia = str(input("Digite o dia em que ele Foi Vacinado: "))
                print()
                anim[idd] = [nome, dia]
                print()
                print("Registrado Com Sucesso!")
                print()
                input("Digite Qualquer Tecla Para Continuar: ")
                
            elif perg == "2":
                print("Muito Bem Você Escolheu Listar os Animais Vacinados")
                print()
                print("Para a segurança de \n de nossos clientes \n Pedimos para que Você digite o ID do animal")
                print()
                idd = str(input("Digite o ID: "))
                if idd in anim:
                    print("Nome:", anim[idd][0])
                    print("Data:", anim[idd][1])
                else:
                    print(" ID não encontrado")
                    
                    input ("Digite Qualquer Tecla Para continuar: ")
                
               
                    
            
            elif perg == "3":
                print("\t\tMuito Bem Você escolheu Atualizar um Animal Já Vacinado\t\t")
                for dados in anim.values():
                     print(dados[0])
                    
                print()
                idd = str(input("Digite o ID do animal: "))
                if idd in anim:
                    nome = input("Digite o novo nome do animal: ")
                    data = str(input("Digite o DIA em que foi vacinado: "))
                    anim[idd][0] = nome
                    anim[idd][1] = data

                    print("Atualizado com sucesso!")
                    input("Digite qualquer tecla para continuar")
                    
                    
            
            elif perg == "4":
                print("\t\tMuito Bem Você escolheu Excluir um animal da lista\t\t")
                idd = str(input("Digite o ID: "))
                if idd in anim:
                    anim.pop(idd)
                    print("Animal excluído com sucesso!")
                else:
                    print("ID não encontrado") 
                    
                    
                    
            elif perg == "0":
                break
            
            
            
            #INFORMAÇOES
    elif perg == "6":
        limpar_tela()
        print("Esse código foi produzido por:")
        print("LUIZ HENRIQUE SOUZA DA SILVA")
        print("do curso de BSI-UFRN 2026.1")
        print("no dia 05/06/2026.")
        print("Sendo Atualizado Constantemente.")
        print()
        print()
        input ("TECLE QUALQUER TECLA PARA CONTINUAR: ")
        
        
        
        #SAIR DO CODIGO
    elif perg == "0":
        break
    
    
print("Fim de Programa")
       
                    
                
##SALVAR CLIENTES ARQUIVOS 
arq_clientes = open("clientes.dat", "wb")
pickle.dump(clientes, arq_clientes)
arq_clientes.close()
