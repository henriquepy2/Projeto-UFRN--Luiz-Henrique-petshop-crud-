from clientes import (
    cadastrar_cliente,
    listar_cliente,
    atualizar_cliente,
    excluir_cliente
)

import servicos as servicos_
import estoque as estoque_
import vacinas as vacinas_
import relatorios as relatorios_ 
import fornecedores as fornecedores_

import os
import pickle


   









import os
import pickle


def limpar_tela():
    if os.name == "nt":
        os.system("cls")
       
    else:
        os.system("clear")
       
def pausa():
    input("Digite qualquer tecla para continuar...")
       
       
       
def recupera_clientes():
    try:
        arq = open("clientes.dat", "rb")
        clientes = pickle.load(arq)
        arq.close()
    except:
        clientes= {
   "001": ["João de Souza", "99597155", "Tob",  "13 de Julho", True],
    "002": ["Maria Betania", "99875541","Bela", "14 de Julho", True],
   "003": ["Chris", "40028922","Fred", "21 de Julho", True],
   "004": ["Roberto", "8499597155", "Roger ", "29 de Setembro", True],
    "005": ["Francisco", "995123442", "Mel", "25 de Agosto", True],
    "006": ["Matheus" , "997822345", "Brutus ", "31 de Agosto", True],
    "007": ["Matias" , "998567994", "Jr", "15 De Setembro", True],
    "008": ["Leonardo" , "9981234455", "Felicia", "1 De Outubro", True],
    "009": ["Bernardo", "994123550", "Bingo", "23 de Outubro", True],
    "010": ["Rocky", "994123550", "Butkus ", "29 de Outubro", True],
    "011": ["Greg", "990155432", "Nelinha", "15 De Novembro", True],
    "012": ["Larissa", "99213456", "Belinha", "20 De Novembro", True],
    "013": ["Larissa", "99213456", "Tom", "10 De Novembro", True],
    "014": ["Marcela", "99817544", "Jerry", "5 De Dezembro", True],
    "015": ["Jaqueline", "99423354", "Guto", "22 de Dezembro", True],
    "016": ["Karoline", "994125699", "Thor ", "23 de Dezembro", True],
    "017": ["Ana Clara", "99108443", "Zeus", "7 de Setembro", True]
   
      }
    return clientes
# ANIMAIS
def recupera_animais():
    try:
        arq = open("anim.dat", "rb")
        anim = pickle.load(arq)
        arq.close()
    except:
        anim = {
        "001": ["Tob", "5 Anos", "28 de Abril",True],
        "002": ["bela", "12 anos", "10 de Abril",True],
        "003": ["fred", "2 anos", "20 de Abril",True],
        "004": ["Roger", "5 anos", "21 de Abril",True],
        "005": ["Mel", "12 Anos", "20 de Janeiro",True],
        "006": ["Brutus", "15 anos", "20 de Junho",True],
        "007": ["JR", "1 ano", "20 de Janeiro ",True],
        "008": ["Felicia", "2 anos", "29 De Janeiro",True],
        "009": ["Bingo", "18 Anos", "27 De Setembro",True],
        "010": ["Butkus", "10 anos", "28 De Outubro",True],
        "011": ["Nelinha", "14 Anos", "29 De junho",True],
        "012": ["Belinha", "3 Anos", "21 De Março",True],
        "013": ["Tom", "1 ano", "22 de Dezembro",True],
        "014": ["Jerry", "6 Anos", "25 de Dezembro",True],
        "015": ["Guto", "3 anos", "28 de Dezembro",True],
        "016": ["Thor", "6 Anos", "21 De Novembro",True],
        "017": ["Zeus", "2 Anos", "10 De Outubro",True],
   
}
    return anim
   
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
   
clientes = recupera_clientes()
servicos = {
    "001": ["Tosa", " R$ 100,00 ",True],
    "002": ["Banho e Tosa", "R$ 150,00",True],
    "003": ["Corte De Unhas", "R$50,00",True],
    "004": ["Limpeza De ouvidos", "R$  40,00",True]

}


fornec = {
    "09231": ["Mars Petcare",True],
    "09113": ["Especial Dog Company",True],
    "21345": ["Pet Nordeste Distribuidora",True],
    "1215432": ["Nova Ração",True],
    "21383": ["Pedigree",True]








}







estoque = {
    "001": ["Ração Royal Canin ", "R$ 25,00",True],
    "002": ["Shampoo" , "R$ 35,00",True],
    "003": ["Petiscos", "R$ 15,00",True],
    "004": ["Coleiras", "R$ 20,00",True],
   
}

anim = recupera_animais()

while True:
    print("="*70)
    print("\t\t\tPrograma Pet shop\t\t\t")
   

    print("\t\t\t1.Módulo Clientes\t\t\t")
    print("\t\t\t2.Módulo Serviços\t\t\t")
    print("\t\t\t3.Módulo de Fornecedores\t\t\t")
    print("\t\t\t4.Módulo De Estoque\t\t\t")
    print("\t\t\t5. Módulo de Vacina\t\t\t")
    print()
    print("\t\t\t6. Relatorios\t\t\t")
    print()
    print("\t\t\t7. INFORMAÇÕES\t\t\t")
   
   
    print()
    print()
    print("\t\t\t0.Sair\t\t\t")
    print("="*70)
   
    print()
    print()
    

    perg = str(input("Digite um Serviço para Escolher: "))
   
   
                 #MODULO CLIENTES
    if perg == "1":
        limpar_tela()
        while True:
            print("="*70)
            print("\t\tMódulo Clientes\t\t")
            print()
            print("\t\t1.Cadastrar Clientes\t\t")
            print("\t\t2.Listar Clientes\t\t")
            print("\t\t3.Atualizar Clientes\t\t")
            print("\t\t4.Excluir Clientes\t\t")
            print("\t\t0.SAIR\t\t")
            print("="*70)
            perg1 = str(input("Digite um serviço para Escolher: "))
   
            if perg1 == "1":
                limpar_tela()
                clientes = cadastrar_cliente(clientes)
                grava_clientes(clientes)
               
                pausa()
       
       
       
   
   
            elif perg1 == "2":
                limpar_tela()
                listar_cliente(clientes)
                   
                pausa()
           
            elif perg1 == "3":
                limpar_tela()
                clientes = atualizar_cliente(clientes)
                grava_clientes(clientes)
                   
                pausa()

                   
                   
                   
                   
                   
            elif perg1 == "4":
                limpar_tela()
                clientes = excluir_cliente(clientes)
                grava_clientes(clientes)
                   
               
                pausa()
                   
                   
                   
            elif perg1 == "0":
                break
               
               
                #MODULO SERVIÇOS
    elif perg == "2":
       
        limpar_tela()
       
        while True:
            print("="*70)
            print("\t\t\t2.Módulo Serviços\t\t\t")
            print()
            print("\t\t1.Cadastrar Serviços\t\t")
            print("\t\t2.Listar Serviços\t\t")
            print("\t\t3.Atualizar Serviços\t\t")
            print("\t\t4.Excluir Serviços\t\t")
            print("\t\t0.SAIR\t\t")
            print("="*70)
       
            perg3 = str(input("Digite Um Serviço Para Escolher: "))
       
            if perg3 == "1":
                limpar_tela()
               
                servicos = servicos_.adicionar_servico(servicos)
               
                pausa()
           
            elif perg3 == "2":
                limpar_tela()
                servicos_.listar_servicos(servicos)
                pausa()

           
       
            elif perg3 == "3":
                limpar_tela()
                servicos = servicos_.atualizar_servicos(servicos)

               
               
           
                pausa()
           
            elif perg3 == "4":
                limpar_tela()
                servicos = servicos_.excluir_servicos(servicos)
                   
                   
                pausa()
               
           
               
            elif perg3 == "0":
                break
               
               
        # MODULO DE FORNECEDORES

    elif perg == "3":
        limpar_tela()
        while True:
            print("="*70)
            print("\t\tBem Vindo Ao Módulo de Fornecedores\t\t")
            print()
            print("\t\t1.Adicionar Fornecedor\t\t")
            print("\t\t2.Listar Fornecedores\t\t")
            print("\t\t3.Atualizar Fornecedores\t\t")
            print("\t\t4.Excluir Fornecedor")
            print("="*70)
            print()

            perg = input("Escolha Um Serviço:  ")

            if perg == "1":
                limpar_tela()
                fornec = fornecedores_.add_fornecedor(fornec)

                pausa()

           
            elif perg == "2":
                limpar_tela()
                fornecedores_.listar_fornecedor(fornec)
                   
                pausa()


                     



            elif perg == "3":
                limpar_tela()
                fornec = fornecedores_.att_fornecedor(fornec)
                   
                pausa()



               
            elif perg == "4":
                limpar_tela()
                fornec = fornecedores_.excluir_fornecedor(fornec)

               
                pausa()

            elif perg =="0":
                break







       
   
       
    # MODULO DE ESTOQUE
    elif perg == "4":
        limpar_tela()
        while True:
            print("="*70)
            print(" \t\t\t4.Módulo de Estoque\t\t\t")
            print()
            print("\t\t1.Adicionar Item ao Estoque \t\t")
            print("\t\t2.Listar Estoque\t\t")
            print("\t\t3.Atualizar Item Do Estoque\t\t")
            print("\t\t4.Excluir Item Do Estoque\t\t")
            print("\t\t0.SAIR\t\t")
            print("="*70)
           
            perg = str(input("Escolhe Um Desses Serviços: "))
           
            if perg == "1":
                limpar_tela()
                   
                estoque = estoque_.add_estoque(estoque)
               
                pausa()
               
               
            elif perg == "2":
                limpar_tela()
                estoque_.listar_estoque(estoque)
                pausa()
                   
                   
           
            elif perg == "3":
                limpar_tela()
                estoque = estoque_.atualizar_estoque(estoque)

                pausa()
               
               
               
           
            elif perg == "4":
                limpar_tela()
                estoque = estoque_.excluir_estoque(estoque)

                pausa()
               
            elif perg == "0":
                break
           
           
           
        #MODULO DE VACINAÇAO
    elif perg == "5":
        limpar_tela()
        while True:
            print("="*70)
            print(" \t\t\t5. Módulo de Vacinação\t\t\t")
            print()
            print("\t\t1. Registrar Vacinação\t\t")
            print("\t\t2. Listar Animais Vacinados\t\t")
            print("\t\t3. Atualizar Animais Vacinados\t\t")
            print("\t\t4. Excluir Animais Vacinados\t\t")
            print()
            print("\t\t0. SAIR\t\t")
            print("="*70)
           
            perg = str(input("Escolha Um Desses Serviços: "))
           
            if perg == "1":
                limpar_tela()
                anim = vacinas_.registrar_vacina(anim)
                grava_animais(anim)
               
                pausa()
               
            elif perg == "2":
                limpar_tela()
                vacinas_.listar_vacina(anim)
                   
                pausa()
               
               
                   
           
            elif perg == "3":
                limpar_tela()
                anim = vacinas_.att_vacina(anim)
                grava_animais(anim)
               
                   
                pausa()
                   
                   
           
            elif perg == "4":
                limpar_tela()
                anim = vacinas_.excluir_vacina(anim)
                grava_animais(anim)
                   
                pausa()
                   
                   
                   
            elif perg == "0":
                break
           
           
           
            #INFORMAÇOES
    elif perg == "7":
        limpar_tela()
        print("="*70)
        print("Esse código foi produzido por:")
        print("LUIZ HENRIQUE SOUZA DA SILVA")
        print("do curso de BSI-UFRN 2026.1")
        print("no dia 05/06/2026.")
        print("Sendo Atualizado Constantemente.")
        print("="*70)
        print()
        print()
        
        pausa()









    elif perg == "6":
         while True:
            limpar_tela()
            print()
            print("="*70)
            print("\t\t1.Relatorio Geral\t\t")
            print("\t\t2.Listagem Com Filtro\t\t")
            print("\t\t3.Filtro + Processamento\t\t")
            print("4 - Combinação de Dados")
            print("0.SAIR")
            print("="*70)

            pp = str(input("Digite o Relatório:  "))

            if pp == "1":
                limpar_tela()

                relatorios_.relatorio_geral(clientes)
               

                pausa()


            elif pp == "2":
                limpar_tela()

                relatorios_.listagem_filtro(clientes)

                pausa()



            elif pp == "3":
                limpar_tela()
                relatorios_.listagem_processamento(anim)

                

                pausa()
               

            elif pp == "4":
                limpar_tela()

                relatorios_.combinacao_dados(clientes, anim)
                pausa()

            elif pp == "0":
                break
           
               
       
       
       
        #SAIR DO CODIGO
    elif perg == "0":
        break
   
   
print("Fim de Programa")
       
                   
               
##SALVAR CLIENTES ARQUIVOS
arq_clientes = open("clientes.dat", "wb")
pickle.dump(clientes, arq_clientes)
arq_clientes.close()

arq_anim = open("anim.dat", "wb")
pickle.dump(anim, arq_anim)
arq_anim.close() 
arq_anim = open("anim.dat", "wb")
pickle.dump(anim, arq_anim)
arq_anim.close()
