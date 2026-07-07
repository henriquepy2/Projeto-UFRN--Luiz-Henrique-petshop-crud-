def registrar_vacina(anim):
    print("\t\t\tMuito Bem Você Escolheu Registrar a Vacinação\t\t\t")
    print()
    idd = str(input("Digite o ID do seu Animal: "))
    if idd in anim:
        print("Já Existe Um usúario Com Esse ID")
                   
    else:
        nome = str(input("Digite o nome do Seu animal: "))
        idade = str(input("Digite A idade Do seu Animal:  "))
        dia = str(input("Digite a data de Vacina: "))
        print()
        anim[idd] = [nome, idade, dia, True]
        print()
        print("Registrado Com Sucesso!")
        print()
    return anim


def listar_vacina(anim):
    print("Muito Bem Você Escolheu Listar os Animais Vacinados")
    print()
    print("Para a segurança de \n de nossos clientes \n Pedimos para que Você digite o ID do animal")
    print()
    idd = str(input("Digite o ID: "))
    if idd in anim:
        if anim[idd][3]:
            print("Nome:", anim[idd][0])
            print("Idade:", anim[idd][1])

        else:
            print("Animal desativado.")
                       
    else:
        ("Id Inválido.")

    return anim


def att_vacina(anim):
    print("\t\tMuito Bem Você escolheu Atualizar um Animal Já Vacinado\t\t")
    for dados in anim.values():
        print(dados[0])
                   
    print()
    idd = str(input("Digite o ID do animal: "))
    if idd in anim:
        if anim[idd][3]:
            nome = input("Digite o novo nome do animal: ")
            idade = str(input("Digite A idade do Seu Animal:  "))
            data = str(input("Digite o DIA em que foi vacinado: "))
            anim[idd][0] = nome
            anim[idd][1] = idade
            anim[idd][2] = data

            print("Atualizado com sucesso!")
                       
        else:
            print("Cliente Desativado.")
                   
                   
                   
    else:
        print("Animal Não Encontrado!!")

    return anim


def excluir_vacina(anim):
    print("\t\tMuito Bem Você escolheu Excluir um animal da lista\t\t")
    idd = str(input("Digite o ID: "))
    if idd in anim:
        print("Nome do Animal: ", anim[idd][0])
        anim[idd][3] = False
        print("Animal excluído com sucesso!")
                   
    else:
        print("ID não encontrado")


    return anim
