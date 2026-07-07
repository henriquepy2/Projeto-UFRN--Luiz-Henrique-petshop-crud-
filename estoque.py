def add_estoque(estoque):
    idd = str(input("Digite o ID do Item:  "))
    if idd in estoque:
        print("Ja Existe Um Item Com Esse ID")
                   
    else:
        add = str(input("Digite um Item Para Ser Adicionado: "))
        preco = int(input("Digite o preço Do item:  "))
               
        estoque[idd] = [add, preco, True]
               
        print("Item Adicionado Com Sucesso!!")

    return estoque

def listar_estoque(estoque):
    idd = str(input("Digite o Id:  "))
    if idd in estoque:
        if estoque[idd][2]:
            print("Nome:", estoque[idd][0])
            print("Preço:", estoque[idd][1])

        else:
            print("Item desativado.")

    else:
        print("Item Não encontrado")
                   
                    
                    

    return estoque


def atualizar_estoque(estoque):
    print("Itens cadastrados:")

    for idd in estoque:
        print("Nome do Item", idd, estoque[idd][0])

    it = input("Digite o ID do item que deseja atualizar: ")

    if it in estoque:
        if estoque[it][2]:
            novo_item = input("Digite o nome do novo item: ")
            preco = str(input("Digite o preço deste Item: "))

            estoque[it][0] = novo_item
            estoque[it][1] = preco
            print("Item atualizado com sucesso!")
                       
        else:
            print("Item Desativado")

    else:
        print("Item não encontrado.")


                    

    return estoque


def excluir_estoque(estoque):
    for idd in estoque:
        print(estoque[idd][0])
                   
    perg = str(input("Qual item Você deseja Apagar De acordo Com ID: "))
               
    if perg in estoque:
        estoque[perg][2] = False
        print("Item excluído com sucesso!")
    else:
        print("Item não encontrado.")
    
    return estoque
