def cadastrar_cliente(clientes):
    idd = str(input("Digite o ID: "))
    if idd in clientes:
        print("Erro! Esse ID já existe.")
    else:
        nome = input("Digite o seu nome: ")
        num = str(input("Digite o seu número: "))
        pet = input("Digite o nome do seu pet: ")
        dia = str(input("Digite APENAS o dia e o Mês que você nasceu:  "))

        clientes[idd] = [nome, num, pet, dia, True]

        print()
        print("Cliente Cadastrado Com Sucesso!")

    return clientes


def listar_cliente(clientes):
    idd = str(input("Digite a ID do cliente: "))
    if idd in clientes:
        if clientes[idd][4]:
            print("Nome do Cliente: ", clientes[idd][0])
            print("Pet: ", clientes[idd][2])
        else:
            print("Cliente desativado.")
    else:
        print("Cliente não encontrado.")


def atualizar_cliente(clientes):
    id_cliente = input("Digite o ID do cliente: ")

    if id_cliente in clientes:
        if clientes[id_cliente][4]:
            nome = input("Digite Seu Nome: ")
            num = input("Digite O seu Telefone: ")
            data = str(input("Digite A data De nascimento: "))
            pet = input("Digite o nome Do Seu pet: ")

            clientes[id_cliente][0] = nome
            clientes[id_cliente][1] = num
            clientes[id_cliente][2] = pet
            clientes[id_cliente][3] = data

            print("Cliente Atualizado Com Sucesso!!")

        else:
            print("Cliente desativado.")

    else:
        print("Cliente Não Encontrado")

    return clientes


def excluir_cliente(clientes):
    excluir = str(input("Digite o ID Da Exclusão:  "))

    if excluir in clientes:
        print("Nome Do cliente: ", clientes[excluir][0])

        clientes[excluir][4] = False

        print("Cliente desativado com sucesso!")

    else:
        print("Cliente não encontrado")

    return clientes
