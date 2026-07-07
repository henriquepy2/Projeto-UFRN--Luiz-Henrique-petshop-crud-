def add_fornecedor(fornec):
    idd = str(input("Digite o IDD:  "))
    if idd in fornec:
        print("Ja existe Um usúario Com Esse Id")
                   
    else:
        add = input("Digite o nome Do fornecedor:  ")
        fornec[idd] = [add, True]

        print()
        print("Fornecedor Adicionado Com Sucesso!!")

    return fornec


def listar_fornecedor(fornec):
    print("Muito Bem Você Escolheu Listar Os nossos Fornecedores")
    id = str(input("Digite O ID: "))            
    if id in fornec:
        if fornec[id][1]:
            print("Fornecedor:", fornec[id][0])
        else:
            print("Fornecedor desativado.")
    else:
        print("Fornecedor não encontrado.")

    return fornec



def att_fornecedor(fornec):
    print("Muito Bem Você Escolheu Atualizar Um Fornecedor")

    id = str(input("Digite o ID desse Fornecedor:  "))

    if id in fornec:
        if fornec[id][1]:
            nome = input("Digite o nome Desse Fornecedor: ")                  
            fornec[id][0] = nome
                       
        else:
            print("Fornecedor Desativado.")

    else:
        print("Fornecedor Não Encontrado")

    return fornec

def excluir_fornecedor(fornec):
    print("Muito Bem Você Escolheu Excluir Um Fornecedor")
    print()
    idd = str(input("Digite o id do Fornecedor:  "))

    if idd in fornec:
        print("Nome do Fornecedor Excluido", fornec[idd][0])
        fornec[idd][1] = False
        print("Fornecedor Excluido Com Sucesso!!!")

               
    else:
        print("Fornecedor Não Encontrado")

    return fornec