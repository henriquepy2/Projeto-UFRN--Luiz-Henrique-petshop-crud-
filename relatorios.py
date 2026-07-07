def relatorio_geral(clientes):
    print("========== RELATÓRIO GERAL ==========")
    print()

    print("ID\tNOME\t\tTELEFONE\tPET\tDIA")
    print("-" * 60)

    for idd in clientes:

        if clientes[idd][4]:
            print(f"ID: {idd}")
            print(f"Nome: {clientes[idd][0]}")
            print(f"Telefone: {clientes[idd][1]}")
            print(f"Pet: {clientes[idd][2]}")
            print(f"Nascimento: {clientes[idd][3]}")
            print("-" * 50)
        else:
            print("Cliente Desativado.")


def listagem_filtro(clientes):
    pet = input("Digite o nome do pet: ")

    print("========== CLIENTES ENCONTRADOS ==========")

    for idd in clientes:
        if clientes[idd][4]:
            if clientes[idd][2].lower() == pet.lower():

                print("ID:", idd)
                print("Nome:", clientes[idd][0])
                print("Telefone:", clientes[idd][1])
                print("Pet:", clientes[idd][2])
                print("Dia:", clientes[idd][3])
                print("---------------------------")


def listagem_processamento(anim):
    print("ANIMAIS COM MAIS DE 10 ANOS")
    print()

    quantidade = 0

    for idd in anim:
        if anim[idd][3]:
            idade = int(anim[idd][1].split()[0])

            if idade > 10:
                print("ID:", idd)
                print("Animal:", anim[idd][0])
                print("Idade:", anim[idd][1])
                print("Vacina:", anim[idd][2])
                print("----------------")

                quantidade = quantidade + 1

    print()

    print("Quantidade de animais com mais de 10 anos:", quantidade)


def combinacao_dados(clientes, anim):
    print("RELATÓRIO CLIENTE + VACINA")
    print()

    print("Cliente\t\tPet\t\tVacina")
    print("-" * 50)

    for idd in clientes:

        if idd in anim:
            if clientes[idd][4] and anim[idd][3]:
                print(f"{clientes[idd][0]}\t\t{clientes[idd][2]}\t\t{anim[idd][2]}")
                    
    
                    
                    
