
listaDePecas = []
#------------------------------- criando a função que efetua o cadastro de peças, colocando as informações passadas em uma lista
#----------------------------------------------------------------
def cadastrarPeca(codigo):          
    print("CADASTRAR PEÇA ")
    nomepeça = input("Informe o nome da peça que deseja cadastrar: ")
    fabricante = input("Informe o fabricante:  ")
    valor = float(input("Informe o valor :  "))
    peça = {"CODIGO": codigo, "NOME": nomepeça,"FABRICANTE": fabricante, "VALOR": valor}
    listaDePecas.append(peça.copy())
    print("Codigo: ", codigo)
    print("Cadastrada com sucesso")
    print("="*50)
#----------------------------------------------------------------

#---------------------------------------------------------------- função para consultar a peça, com um mini menu, e com if e elif de acordo com 
#---------------------------------------------------------------- o digitado pelo usuario, verificando no primeiro if, todas as peças, recorredo ao for para mostrar todos
#---------------------------------------------------------------- os itens da lista. Consulta de peças por codigo que utiliza o for na lista, e deixa o if perguntado se o codigo
#---------------------------------------------------------------- digitado pelo usuario, for igual ao da lista, ele exibe




def consultarPeca():
    while True:
        try:

            print("CONSULTA DE PEÇAS ")
            consuPecas = int(input("Opção desejada\n"
                                    "1- Consultar todas as peças\n"
                                    "2- Consultar peças por código\n"
                                    "3- Consultar peças por Fabricante\n"
                                    "4- Retornar\n"))
            print("="*50)
#verificando no primeiro if, todas as peças, recorredo ao for para mostrar todos
#os itens da lista. 
            if consuPecas == 1:
                print("CONSULTA DE TODAS AS PEÇAS ")
                for peça in listaDePecas:  
                   for key, value in peça.items(): 
                        print("{}:{}".format(key, value))
                        print("="*50)
#Consulta de peças por codigo que utiliza o for na lista, e deixa o if perguntando se o codigo
# digitado pelo usuario é igual o da lista, se caso afirmativo, ele exibe


            elif consuPecas == 2:
                print("CONSULTA DE PEÇAS POR CODIGO ")
                entrada = int(input("Digite o código: "))
                print("="*50)
                for peca in listaDePecas:  # selecionar cada dicionário da minha lista
                    if(peca["CODIGO"] == entrada):
                        for key, value in peca.items():
                            print("{}:{}".format(key, value))
                            print("="*50)

                    elif (peca["CODIGO"] != entrada):
                      print("Este código não existe, ou já foi removido.")
                      print("="*50)

#consulta de peças por fabricando, utiliando o mesmo metodo anterior, mas agora o if passa perguntando se na chave fabricante, existe algum termo
#igual ao digitado pelo usuario, se caso for afirmativo, ele imprime a chave e o respectivo valor;

            elif consuPecas == 3:
                print("CONSULTA DE PEÇAS POR FABRICANTE ")
                entrada = input("Digite o fabricante: ")
                for peca in listaDePecas: 
                    if(peca["FABRICANTE"] == entrada):
                        for key, value in peca.items():
                            print("{}:{}".format(key, value))
                            print("="*50)
#caso a opção for 4, ele retorna ao menu principal.
            elif consuPecas == 4:
                print("Retornando ao menu...")
                print("="*50)
                return
            else:
                print("Opção não encontrada..")
                print("="*50)
                continue
        except ValueError:
            print("o valor digitado não é inteiro, tente novamente.")
            print("="*50)
#-----------------------------------------------------------------------------------
#função para remover a peça
def removerPeca():
    print("REMOVER PEÇAS ")
    entrada = int(input("Digite o código a ser removido: "))
    print("="*50)
#utilizando o for para verificar no dicionario, se existe alguma chave com o codigo = ao que o usuario digitou, se caso for afirmativo, ele executa o .remove 
#na peça
    for peca in listaDePecas:  
        if(peca["CODIGO"] == entrada):
           listaDePecas.remove(peca)
           print("Peça removida com sucesso!")
           print("="*50)

        return
#-----------------------------------------------------------------------------------


print("CONTROLE DE ESTOQUE RU: 4045314 \n"
"Vinicius Falcão")
codigo = 0
while True:
    try:
        opcao = int(input("Digite a opção  desejada: \n"
                        "1- Cadastrar peça\n"
                        "2- Consultar peça\n"
                        "3- Remover peça\n"
                        "4- Sair \n"))
        
#aqui ele vai definir que cada codigo dentro do dicionario, vai ser somado +!, assim tornando uma sequencia de cada peça registrada
#ex: peça1, peça2, peça3..
        if opcao == 1:
            codigo = codigo + 1
            cadastrarPeca(codigo)
 #os elifs vão executando as funções, conforme digitado pelo usuario
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print("Encerrando o programa!!!!")
            break
        else:
            print("Opção invalida")
            continue
    except ValueError :
        print("O valor digitado não é numerico, tente novamente por favor. ")
#-------------------------------------------------------------------------------------
