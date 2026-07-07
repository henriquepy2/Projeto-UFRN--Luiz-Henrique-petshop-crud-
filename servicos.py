def adicionar_servico(servicos):
    serv1 = str(input("Digite o ID do Serviço:  "))
    if serv1 in servicos:
        print("Ja existe Um usúario com Esse ID")
               
    else:
        serv = input("Qual Novo Serviço Você Quer colocar: ")
        preco = str(input("Digite o Preço Do serviço:  "))
           
        servicos[serv1] = [serv, preco, True]

    return servicos

def listar_servicos(servicos):
    idd = str(input("Digite o ID do serviço:  "))
    if idd in servicos:
        if servicos[idd][2]:
            print("Nome:", servicos[idd][0])
            print("Preço:", servicos[idd][1])

        else:
            print("Serviço desativado.")
                       
    else:
        print("Id inválido")
    
        
    

    return servicos


def atualizar_servicos(servicos):
    for id in servicos:
        print(id, servicos[id][0])

    id_servico = input("Digite o ID do serviço que deseja atualizar: ")

    if id_servico in servicos:
        if servicos[id_servico][2]:

            novo_servico = input("Digite o novo nome do serviço: ")
            preco = input("Digite o novo preço do serviço: ")
            servicos[id_servico][0] = novo_servico
            servicos[id_servico][1] = preco
            print("Serviço atualizado com sucesso!")
                       
        else:
            print("Serviço Desativado.")
               
    else:
        print("Serviço não encontrado.")

                
                
            
    return servicos




def excluir_servicos(servicos):
    for idd in servicos:
        print(idd, servicos[idd][0])
    idd = str(input("Digite o ID do serviço que Você quer Excluir: "))
               
    if idd in servicos:
        servicos[idd][2] = False
        print("Serviço Excluido Com Sucesso!!")
                   
    else:
        print("Serviço não encontrado. ")

 
    return servicos
