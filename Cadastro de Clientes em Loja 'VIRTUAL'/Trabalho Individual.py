#TRABALHO INDIVIDUAL - JOAO ICARO MOREIRA LOIOLA
#MATRICULA 537176

import time
from datetime import datetime

def reaData(): #LER ARQUIVO DE TEXTO
    a = open('dados.txt', 'a')     #cria o arquivo dados.txt 
    a.close()                      #fecha o mesmo arquivo
    read = open('dados.txt', 'r')  #abre o arquivo dados.txt no modo de leitura 
    data = read.readlines()        #lê o arquivo dados.txt
    read.close()                   #fecha o arquivo 
    return data

def register(): #CADASTRAR UM USUÁRIO NOVO 

    #PRINT DE UM PEQUENO CABEÇALHO
    print('\n' + 'INSIRA SEUS DADOS ABAIXO!' + '\n')   

    #NOME COMPLETO E LOGIN DO CLIENTE
    fullName = str(input('Nome completo: ')).strip().title()
    login = str(input('Crie seu Login: ')).strip()

    data = reaData()    #chamar a função
    
    #CONFERIR O LOGIN NO ARQUIVO DE TEXTO
    for user in data:
        user = eval(user)
        if user['login'] == login:
            print(f'\nLogin ja existente, escolha outro!')
            time.sleep(1)
            return menu()
    
    #INPUTS DE CADASTRO
    password = input('Crie sua senha: ').strip()
    email = input('Insira seu E-mail: ').strip()
    bornDay = input('Insira sua data de nascimento: ').strip()
    cellphone = input('Insira seu telefone para contato: ').strip()

    print('\nAGORA IREMOS INSERIR SEUS DADOS DE ENTREGA!\n')
    time.sleep(1)

    street = input('Rua: ').strip().title()
    number = input('Numero: ').strip().title()
    complement = input('Complemento: ').strip().title()
    district = input('Bairro: ').strip().title()
    city = input('Cidade: ').strip().title()
    postalCode = input('CEP: ').strip().title()
    reference = input('Ponto de Referencia: ').strip().title()

    #ARMAZENAR TUDO EM UM DICIONÁRIO
    dictDados = {   
    'nome': fullName,
    'login':login, 
    'senha':password,
    'email':email,
    'data nasc':bornDay,
    'telefone':cellphone,
    'Rua':street,
    'Numero':number,
    'Complemento':complement,
    'Bairro':district,
    'Cidade':city,
    'CEP':postalCode,
    'Ponto de Referencia':reference
    }
    
    #escrever o dicionario no final do arquivo (nova linha)
    with open('dados.txt', 'a', encoding='utf-8') as dadosUsuario:
        dadosUsuario.writelines(str(f'{dictDados}\n'))

    print('\nUsuario cadastrado com sucesso!')
    time.sleep(1)
    
    return menu()

def showData(): #MOSTRAR DADOS DO CLIENTE   
    
    login = input('Insira seu Login: ')    #INSERIR LOGIN
    data = reaData()                       #CHAMAR A FUNÇÃO DE LER ARQUIVO

    for user in data:  #para cada linha no arquivo                    
        user = eval(user) #eval avalia a cadeia de caracteres (string) e identifica-as como dicionarios
        if user['login'] == login: #se o indice 'login' do dicionario for igual ao que o usuario entrou, entao...
            print(f'\nDados do login: {login}' + '\n') 
            for item, dado in user.items(): #printa o indice 0 e 1 do dicionario
                print(f'{item}: {dado}') #...
            time.sleep(2) 
            return menu()
    print('Login nao encontrado, insira QUALQUER valor para retornar ao menu')
    opcao = input('') #pequeno condicional para voltar ao menu
    if opcao == '':
        return menu()
    else:
        return menu()

def showCustomers(): #MOSTRAR CLIENTES CADASTRADOS

    data = reaData() #ler arquivo na variavel data
    keyNome = 'nome' #define o indice 0 do dicionario
    keyLogin = 'login' #define o indice 1 do dicionario 
    print(f'\nUSUARIOS CADASTRADOS' + '\n')
    for user in data: #para cada linha no arquivo
        user = eval(user) 
        print(f'Nome: {user[keyNome]} /// Login: {user[keyLogin]}\n') #imprima o nome da pessoa e o login
    opcao = input('Insira qualquer valor para retornar ao menu: ') #pequeno condicional para voltar ao menu
    if opcao == '':
        return menu()
    else:
        return menu()
        
def report(): #CRIAR RELATÓRIO

    report = open('clientes.txt', 'w', encoding='utf-8') #abrir e sobrescrever o arquivo 'clientes.txt'
    data = reaData() #ler arquivo
    clientes = 0 #valor inicial para variavel clientes

    for l in data: #cada vez que passar por uma linha no arquivo, ela receberá + 1
        clientes += 1

    report.writelines(f'''Relatório de Clientes
        
A loja Loiola Express possui {clientes} clientes que estao listados abaixo\n\n''') #print do cabeçalho com o numero de clientes
    
    count = 0 #contador para prefixo 1., 2., 3., 4. de cada usuário
    for user in data: #para cada item no dicionario
        count += 1 #contador recebe +1
        user = eval(user) #transforme em dicionario
        keyNome = user['nome'] #defina que keyNome é o indice 'nome' do dicionario
        report.writelines(f'{count}. <{keyNome}>\n') #escreva o valor count com um '.' e o nome completo entre <>
    report.writelines('\n' + datetime.today().strftime(f'Russas, %d do %m de %Y')) #print da data atual
    report.close() #feche o arquivo de texto

    #PLUS:

    with open('clientes.txt', 'r', encoding='utf-8') as r: #abra o arquivo no modo de leitura
        reporting = r.read() #crie uma variavel que leia o arquivo inteiro
        print(reporting) #imprima a variavel no terminal
    print(f'\nAperte qualquer tecla para retornar ao menu')
    opcao = input('')
    if opcao == '': #pequena condicional para voltar ao menu
        return menu()
    else:
        return menu()

def menu():        #CRIA UM MENU INTERATIVO DE MÚLTIPLAS ESCOLHAS

    print(f"""\n\033[35m           SEJA BEM VINDO! \033[m\n
**********\033[34m Loiola Express \033[m**********
* \033[32m[1] Cadastrar cliente            \033[m*
* \033[32m[2] Mostrar dados do cliente     \033[m*
* \033[32m[3] Mostrar clientes cadastrados \033[m*
* \033[32m[4] Gerar relatório dos clientes \033[m*
* \33[31m[0] Sair                         \33[m*
************************************""")
    try:                                             #TENTE
        opcao = int(input('Opção: '))                #INPUTAR ISSO
    except ValueError:                               #CASO INPUTEM ERRADO
        print('Caractere Invalido, Tente novamente!')#IMPRIMA ISSO
        time.sleep(1)                                #FAÇA ISSO
        return menu()                                #E VOLTE PRO INICIO...
    else:                                            #caso contrário...

        while True:                                  #enquanto for verdade
            if int(opcao) == 1:                      #se o valor que o usuario digitou, for 1:
                register()                           #abra a funcao register
                return
            elif int(opcao) == 2:                    # -------------
                showData()                           # -------------
                return             
            elif int(opcao) == 3:                    # -------------
                showCustomers()                      # -------------
                return 
            elif int(opcao) == 4:                    # -------------
                report()                             # -------------
                return
            elif int(opcao) == 0:                    #se o valor inserido for 0, feche o programa
                print(f"\nObrigado por usar nosso Software!\nVolte em breve!\nEncerrando...\n")
                time.sleep(1)
                break
            else:                                    #se nao for nenhum desses, tente novamente
                print("Digite um dos números acima!")
                time.sleep(1)
                return menu()
        return

menu() #chamar menu