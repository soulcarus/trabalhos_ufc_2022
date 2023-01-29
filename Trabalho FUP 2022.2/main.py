#TRABALHO DE FUNDAMENTOS DA PROGRAMAÇÃO
#JOAO ICARO MOREIRA LOIOLA - 537176
#MARIA EDUARDA NOGUEIRA - 536868 
#AMCC - Armazém de Materiais de Construção Civil

import inquirer #!pip install inquirer
import time
import os 

lista_de_dicionarios = []
setores = ['civil','pintura e acabamento','refrigeracao','eletricos']

def Arquivo_Modo_Append(): 
    arquivo = open('estoque.txt','a') 
    return arquivo                    #faz todo o conteudo da variavel acima ser retornado quando a função chamar

def limparTerminal():
    os.system('cls') #da um 'clear' no terminal
    print(4*'\n')    #pula 4 linhas pra ficar centralizado

def Receber_Linhas_do_Arquivo():           
    arquivo = open('estoque.txt','r')   #abre o arquivo no modo R
    textos = arquivo.readlines()        #armazena as linhas do arquivo na variavel textos
    arquivo.close()                     #fecha o arquivo
    return textos                       #retorna a variavel com as linhas quando chamada

def Verificar_se_Nome_Existe(nome):                                    #recebe uma variavel para ser o 'nome'
    for prod in lista_de_dicionarios:                        #para cada dicionario na lista de lista_de_dicionarios
        if nome.upper() == prod['descricao']:                        #verifique se a chave 'nome' de cada um deles corresponde a variavel que a funcao recebe
            print('Nome Já Existe! Retornando ao Menu!🙁')   #se for verdade, o produto ja esta cadastrado, volta ao menu
            time.sleep(1)                                    #demora 2 segundos
            return True                                      #retorna/armazena TRUE indicando que existe 
    return False                                             #caso o nome nao existe, armazene/retorne falso na funcao

def AdicionarProdutos_naLista():   
    lista_de_dicionarios.clear()         #limpa a lista, caso exista alguma anterior
    linhas = Receber_Linhas_do_Arquivo()        #le o arquivo e armazena o return na variavel linhas (retornamos o readlines)
    for linha in linhas:                 #para cada linha do arquivo
        dados = linha.split(' | ')       #os dados das linhas vão ser separados em 4 partes pelo " - "
        produto ={
            'setor': (dados[0].strip()),
            'descricao': dados[1].strip(),
            'quantidade': int(dados[2].strip()),
            'valor': float(dados[3].strip())
        }                                       #cria-se um dicionario contendo setor, 'nome', qtd e valor
                                                #armazena cada uma das partes separadas por " - " dentro do dicionario
        lista_de_dicionarios.append(produto)    #adiciona esse dicionario a lista de dicionarios

def Cadastrar_Produto():

    AdicionarProdutos_naLista()         #le o arquivo e cria a lista
    limparTerminal()                            #limpa terminal

    print('Voce selecionou: ADICIONAR PRODUTO😆\n')
    #utilizacao do modulo inquirer para criar um pequeno menu de seleção
    setor = inquirer.list_input("Qual o setor?🤔", choices=['civil', 'pintura e acabamento', 'eletricos', 'refrigeracao','cancelar 👎'])

    #caso a opcão selecionada seja a de cancelar, retorne o menu
    if setor == 'cancelar 👎':
        print('Retornando ao menu!🙁')      #avise que iremos ao menu
        time.sleep(1)                        #espere 2 segundos
        menuPrincipal()                      #execute o menu

    #caso o usuario tenha escolhido alguma das opcoes, execute:
    else:
        limparTerminal()                                 #limpe o terminal
        arquivo = Arquivo_Modo_Append()                  #armazene o return da função dentro de arquivo
        descricao = input('Qual o nome do produto?🤨\nNome: ')    #pergunte o nome do produto
        verificador = Verificar_se_Nome_Existe(descricao)          #verifique se o nome existe, se existir, retornará True

        if  verificador == False:                                              #caso retorne falso, cadastre o produto
            quantidade = int(input('\nQuantos desse item deseja adicionar?💁\nQuantidade: '))   
            valor = float(input('\nQual o valor do produto?🙅\nPreço: '))        
            arquivo.write("{:20} | {:15} | {:9}        | {:7.2f}\n".format(setor,descricao.upper(),quantidade,valor))
            arquivo.close()                                          #aplique as alterações no arquivo
            print('\nConcluído! Retornando ao menu!...🙌')
            time.sleep(1)         

def mostrarlista_de_dicionarios():

    limparTerminal()                        #limpa o terminal
    #AQUI VAMOS ATUALIZAR A LISTA
    AdicionarProdutos_naLista()     #preenche a lista de acordo com as linhas do arquivo

    #print do menu
    print(8*'   ' + 'ESTOQUE DO ARMAZEM '+ '\n'+ 66*'_'+ '\n')
    print('{:20s} | {:15s}|   {:14s}| {:5s} \n'.format('Setor','Descrição','Quantidade','Valor') + 66*'_' + '\n')
    #para cada dicionario da lista, printe as seguintes informações deles:
    for prod in lista_de_dicionarios:
        print("{:20} | {:15}|{:9}        |{:7.2f}".format(prod['setor'],prod['descricao'],prod['quantidade'],prod['valor']))

def reescreverArquivo(arquivo,adicional):
    arq = open('estoque.txt','w')
    arq.writelines(arquivo)
    arq.writelines(adicional)
    arq.close()

def removerItemDoEstoque():

    AdicionarProdutos_naLista()     #preenche a lista de acordo com as linhas do arquivo

    arquivo_de_texto = Receber_Linhas_do_Arquivo() #armazena o return da função na variavel arquivo_de_texto
    limparTerminal()

    print('VOCE SELECIONOU: REMOVER ITEM DO ESTOQUE😼\n')
    #escolher o setor
    setor = inquirer.list_input("Em que setor esta o produto?💁‍♀️", choices=['civil', 'pintura e acabamento', 'eletricos', 'refrigeracao','cancelar 👎'])
    #se ele quiser cancelar, cancele
    if setor == 'cancelar 👎':
        print('Retornando ao menu!🙁')
        time.sleep(2)
        menuPrincipal()
    #crie uma lista vazia
    nomes = []

    #para cada dict na lista de dicts...
    for cada_dict in lista_de_dicionarios:  
        if cada_dict['setor'] == setor: #se o setor inserido for igual ao setor de algum dict...
            nomes.append(cada_dict['descricao'])   #adicione o nome desse dict da linha anterior, na lista nova dos NOMES de produtos.

    #CASO NAO TENHA NENHUM ITEM DENTRO DA LISTA NOMES
    if len(nomes) == 0:  #SIGNIFICA QUE NAO FOI ADICIONADO NENHUM NOME NO '''FOR''' ANTERIOR, OU SEJA, NAO EXISTE NADA!
        print('Nenhum produto cadastrado!🙅') #SE NAO EXISTE NADA, NAO HA PRODUTO CADASTRADO NO SETOR
        time.sleep(1)                       #PAUSA POR UM SEGUNDO
        return removerItemDoEstoque()       #VOLTA PARA O INICIO DO MENU
            
    #caso exista itens dentro: rode as seguintes linhas
    counto = 0
    
    limparTerminal()
    descricao = inquirer.list_input("Escolha o produto", choices=[*nomes])

    #PARA CADA DICIONARIO NA LISTA DE DICIONARIOS
    for cada_produto in lista_de_dicionarios:   #SE O SETOR DO DICIONARIO E O NOME BATEREM COM OS INSERIDOS PELO USUARIO...
        if cada_produto['setor'] == setor and cada_produto['descricao'] == descricao:
            quantidade = cada_produto["quantidade"] #ARMAZENE A QUANTIDADE DE ITENS DESSE PRODUTO NA VARIAVEL QUANTIDADE

    escolha = inquirer.list_input("O que deseja? ",choices=['[0] Remover quantidade especifica','[1] Remover tudo'])
    
    #PARA CADA LINHA DO ARQUIVO...
    for linha in arquivo_de_texto:
        if setor in linha and descricao in linha: #SE O SETOR E A DESCRICAO ESTIVER NA MESMA LINHA...
            if '1' in escolha:                    #caso a pessoa tenha escolhido a opcao 1...
                print(f'Deletando... \nitem: {descricao} \nsetor: {setor}')
                time.sleep(2)
                del arquivo_de_texto[counto]      #delete a linha tal do arquivo de texto
                reescreverArquivo(arquivo_de_texto,'')     #reescreva o arquivo de texto sem a linha (aspas vazias)

            if '0' in escolha:                     #se a pessoa escolheu 0
                qtd = int(input(f'Quantos deseja remover? Maximo de {quantidade} unidades \nQuantidade: '))
                if qtd > quantidade:
                    print('Nao existem tantas unidades deste item! ')
                    time.sleep(1)
                elif qtd == 0 or qtd < 0:
                    print('Não há o que remover')
                    time.sleep(1)
                elif qtd == quantidade:
                    print('Era so ter marcado opcao [0] cara, removendo...')
                    time.sleep(2)
                    del arquivo_de_texto[counto]
                    reescreverArquivo(arquivo_de_texto,'')
                    time.sleep(1)
                elif qtd < quantidade and qtd > 0: #SE FOR UM VALOR VALIDO
                    print('\nQUANTIDADE ALTERADA COM SUCESSO!')
                    time.sleep(1)
                    linha = linha.replace(f"{quantidade}",f"{quantidade-qtd}") #troque o caractere que contem a quantidade antiga pela nova
                    del arquivo_de_texto[counto]                   #delete a linha antiga
                    reescreverArquivo(arquivo_de_texto,linha)      #reescreva o arquivo sem a linha antiga e adicione a nova (linha)
                else: #caso nao valide nenhuma das opcoes, volte ao inicio da funcao
                    continue
        counto += 1 #contador das linhas aumenta cada vez que nao encontra a linha do 'if setor in linha and descricao in linha'

def menuPrincipal():
    while True:
        Arquivo_Modo_Append()
        limparTerminal()
        print('''AMCC - Armazém de Materiais de Construção Civil\n''')
        opcao = inquirer.list_input("Escolha uma opcao", choices=['Cadastrar um novo produto✅', 'Listar cadastrados👀', 'Remover ítem do estoque❌', 'Sair🏃💭'])

        if opcao == 'Cadastrar um novo produto✅':
            Cadastrar_Produto()
        elif opcao == 'Listar cadastrados👀':
            mostrarlista_de_dicionarios()
            opcao = input('\nAperte ENTER para retornar ao menu!')
        elif opcao == 'Sair🏃💭':   
            print('Obrigado por usar nosso programa!👋')
            quit()
        elif opcao == 'Remover ítem do estoque❌':
            removerItemDoEstoque()

menuPrincipal() 