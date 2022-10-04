#POCS (Programa Operacional integrado com o ramo farmacêutico SOS)
#Desenvolvedora </DevNbesties>
#Maria Eduarda, João Ícaro, Átila Silvio, Francisco Levi e Francisco José
#Funcionalidades: Gerenciar o Decréscimo do número de produtos por meio de um fluxo
#de saída e o acréscimo de quantidade por meio do cadastramento de produtos.

import time 

#FUNÇÕES: 

def abrirtxt(): #função para abrir o arquivo do inventário no modo leitura e armazenar a uma variável
    dcinventario = open('inventario.txt', 'r')
    dados = dcinventario.readlines()
    dcinventario.close()
    return dados

def cadastro(): #cadastrar item no inventario
    try:
        nomeProduto = str(input("Digite o nome do produto desejado: ")).strip()
        dosagem= str(input('Digite a dosagem do produto e sua unidade (ml/mg): ')).strip()
        qtd= int(input('Digite a quantidade do produto: '))
        preco = float(input("Digite o valor do produto desejado: "))
    except ValueError as error:
        print('\nInformação Inválida, tente novamente!')
        time.sleep(1)
        return MenuPrincipal()
    else:
        escrever=open('inventario.txt','a')
        dados = abrirtxt()

        for dado in dados:        #percorrer cada linha do inventario
            dado = eval(dado)     #transformar a linha que está percorrendo em dict
            if (dado['nome'] == nomeProduto and dado['dosagem'] == dosagem): #verificar se o nome e a dosagem conferem
                print(f'\nProduto ja esta cadastrado')
                time.sleep(1)
                escrever.close()
                return MenuPrincipal()

        loginsDicionario = {'nome': nomeProduto, 'dosagem': dosagem, 'quantidade': qtd, 'preco': preco}
        print('Produto cadastrado com Sucesso! Retornando ao menu')
        time.sleep(1)
        escrever.writelines(str(f'{loginsDicionario}\n'))
        escrever.close()
    return MenuPrincipal()

def descadastro(): #remover um item do inventario de medicamentos
    nomeproduto=str(input('\nDigite o nome do medicamento: ')).strip()
    dosagem=str(input('\nDigite a dosagem do produto (ml/mg): ')).strip()
    
    dados = abrirtxt()
    count = 0

    for dado in dados:
        dado = eval(dado)
        if dado['nome'] == nomeproduto and dado['dosagem'] == dosagem:
            del dados[count]
            print('\nSucesso!'+ '\n')
            time.sleep(1)
            arq = open('inventario.txt', 'w')
            arq.writelines(dados)
            return (dados) 
        count += 1 

    print('\n' + 'Produto nao existe!'+ '\n')
    time.sleep(2)
    return MenuPrincipal()
    
def atualizarCadastrados(): #atualizar algumas informações de tal produto cadastrado
    nomeproduto=str(input('\nDigite o nome do medicamento que deseja alterar: ')).strip()
    dosagem=str(input('\nDigite a dosagem do produto (ml/mg): ')).strip()

    dados = abrirtxt()
    count = 0

    for dado in dados:
        dado = eval(dado)
        if dado['nome'] == nomeproduto and dado['dosagem'] == dosagem:
            print('\n****************************************')
            print("""\nINSIRA A NOVA QUANTIDADE E O NOVO PREÇO!"""+ '\n')
            print('****************************************\n')
            del dados[count]
            qtdNova = int(input('Digite a quantidade nova: '))
            valorNovo = float(input('\nDigite o valor novo: '))
            dictNovo = {'nome': nomeproduto, 'dosagem': dosagem, 'quantidade': qtdNova, 'preco': valorNovo}
            print('\nSucesso!'+ '\n')
            time.sleep(1)
            arq = open('inventario.txt', 'w')
            arq.writelines(dados)
            arq.close()
            arq1 = open('inventario.txt', 'a')
            arq1.writelines(str(dictNovo) + '\n')
            arq1.close()     
            return dados
        count += 1 
    else:
        print('Produto nao existe!')
        time.sleep(1)
        return MenuPrincipal()

def MenuPrincipal(): #menu interativo que sempre será chamado ao iniciar
    print('''
********************************
*           P O C S            *
********************************
*                              *
* \033[1;32m[1] CADASTRAR UM PRODUTO\033[m     *
* \033[1;32m[2] DAR BAIXA EM PRODUTO\033[m     *
* \033[1;32m[3] ATUALIZAR ITEM          \033[m *
* \033[1;91m[0] ENCERRAR SOFT. POCS\033[m      *
*                              *
********************************
''')
    
    while True:
        try:
            opção = int(input('Digite sua opção: '))
        except ValueError as error:
            print('\nValor Inválido')
            time.sleep(2)
            return MenuPrincipal()
        else:
            if opção == 1:
                cadastro()
                return

            elif opção == 2:
                descadastro()
                return MenuPrincipal()

            elif opção == 3:
                atualizarCadastrados()
                return MenuPrincipal()

            elif opção == 0:
                print('\nEstamos encerrando o programa. Até logo!\n')
                break

            else:
                print('OPÇÃO INVALIDA')
                time.sleep(1)
                return MenuPrincipal()

MenuPrincipal()