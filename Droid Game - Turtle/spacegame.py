'''
Aluno: João Ícaro Moreira Loiola
Matrícula: 537176
Trabalho 1 - 2022.2
'''

import turtle
import random

#CRIAR JANELA
janela = turtle.Screen()
janela.bgpic("background.gif") #DEFINIR FUNDO
janela.setup(360,640)          #DEFINIR TAMANHO
janela.title('Droid Game')     #DEFINIR TITULO
janela.tracer(0)               #CANCELAR ANIMAÇÕES

#DEFINIR VARIAVEIS DAS PONTUAÇÕES
gas = 50
distancia = pontuacao = contador = 0

def movimentoDireita():  #FUNÇÃO CHAMADA AO APERTAR A TECLA 'D'
   if nave.xcor() < 150: #CASO A NAVE ESTEJA A ESQUERDA DE 150:
        nave.forward(5)  #A NAVE PODERÁ ANDAR PARA A DIREITA

def movimentoEsquerda():   #FUNÇÃO CHAMADA AO APERTAR A TECLA 'A'
    if nave.xcor() > -150: #CASO A NAVE ESTEJA A DIREITA DE -150:
        nave.back(5)       #A NAVE PODERÁ ANDAR PARA A ESQUERDA

def adicionarShapes():     #ADICIONA TODOS OS GIFS DO JOGO
    janela.addshape('nave.gif')         
    janela.addshape('asteroide1.gif')    
    janela.addshape('asteroide2.gif')
    janela.addshape('coca.gif')        
    janela.addshape('explosion1.gif')
    janela.addshape('explosion2.gif')
    janela.addshape('explosion3.gif')
    janela.addshape('explosion4.gif')

adicionarShapes() #CHAMA A FUNÇÃO INSTANTANEMENTE      
   
def instrucoes():     #FUNÇÃO PARA MOSTRAR AS INSTRUÇÕES NA TELA

    titulo.setx(-200) #DEFINIR O X DO TITULO COMO -200
    #ESCREVER AS INSTRUÇÕES:
    titulo.write('''
          INSTRUÇÕES



    'A' MOVE PARA <-------
    'D' MOVE PARA ------->
    COLETE TODAS AS COCAS!
    FIQUE ATENTO AO FUEL 0
''',font=('Courier', 16, 'bold'))
    #DEFINIR POSIÇÕES X E Y DO PLACAR
    placar.setx(-165)
    placar.sety(-150)
    #FAZER O PLACAR ESCREVER UMA MENSAGEM
    placar.write('PRESSIONE ESPAÇO PARA PROSSEGUIR',font=fontePlacar)

    janela.onkeypress(lobby,'space') #PRESSIONAR A TECLA ESPAÇO CHAMA A FUNÇÃO 'LOBBY'

def lobby(): #FUNÇÃO PARA ESCREVER UM MINI 'LOBBY'  

    titulo.clear() #APAGA O TITULO ESCRITO ANTERIORMENTE
    placar.clear() #APAGA O MENU ESCRITO ANTERIORMENTE
    titulo.goto(-135, 0)   #ENVIA O TITULO PARA X e Y
    titulo.color('orange') #DEFINE NOVA COR PARA TITULO
    #ESCREVE:
    titulo.write('PRESSIONE ESPAÇO!', font=fonteTitulos)
    placar.goto(-132,-30)  #ENVIA O PLACAR PARA X e Y
    #ESCREVE:
    placar.write('developed by: git @icarufc', font=('courier', 12, 'bold'))
    placar.goto(0,200)     #ENVIA O PLACAR PARA X e Y
    titulo.color('white')  #DEFINE COR NOVA DO TITULO
    #AO PRESSIONAR ESPAÇO, CHAME A FUNÇÃO "INICIAR JOGO"
    janela.onkeypress(IniciarJogo, 'space')

#CRIAÇÃO DA NAVE (mesmo modelo para o resto dos itens)

nave = turtle.Turtle()
nave.shape('nave.gif') #DEFINE O FORMATO (IMAGEM .GIF)
nave.penup()           #PARAR DE RISCAR O 'PAPEL'
nave.setx(0)           #DEFINE X 
nave.sety(-200)        #DEFINE Y

#CRIAR FONTES (TUPLAS COM AS INFORMAÇÕES)
fontePlacar = ('Courier', 13, 'bold')
fonteTitulos = ('Courier', 20, 'bold')

#CRIAR PLACAR
placar = turtle.Turtle()
placar.ht()
placar.penup()
placar.goto(0, 200)
placar.color('white')

#CRIAR UM CONTADOR PARA O PLACAR
contador_placar = turtle.Turtle()
contador_placar.penup()
contador_placar.ht()
contador_placar.goto(-120, 230)
contador_placar.color('white')

#CRIAR UM TITULO PARA O TEXTO PRINCIPAL
titulo = turtle.Turtle()
titulo.ht()
titulo.penup()
titulo.color('white')
titulo.goto(-130, 0)

#chame a função instruções (após criar os titulos)
instrucoes()

#CRIAR ASTEROIDE #1
asteroide = turtle.Turtle()
asteroide.penup()
asteroide.shape('asteroide1.gif')
asteroide.right(90) 

#CRIAR ASTEROIDE #2
asteroide2 = turtle.Turtle()
asteroide2.penup()
asteroide2.shape('asteroide2.gif')
asteroide2.right(90)

#CRIAR GASOLINA
gasolina = turtle.Turtle()
gasolina.penup()
gasolina.shape('coca.gif')
gasolina.right(90)

#CRIAR UMA MINI COCA PARA O PLACAR DE COCA
coca_placar = turtle.Turtle()
coca_placar.penup()
coca_placar.shape('coca.gif')
coca_placar.goto(-140,240)

def IniciarJogo():    #FUNÇÃO PARA TDO COMEÇO E RECOMEÇO DE JOGO

    #chama as variaveis para a função
    global gas
    global distancia
    global pontuacao
    global contador

    #define os valores delas como o seu valor inicial
    gas = 50
    distancia = pontuacao = contador = 0

    #apaga qualquer coisa escrita com o contador_placar
    contador_placar.clear()
    #envia o contador_placar para tal coordenada
    contador_placar.goto(-120, 230)
    #apaga qualquer coisa escrita com o titulo
    titulo.clear()
    #apaga qualquer coisa escrita com o placar
    placar.clear()

    #define o shape da nave como 'nave.gif', pois seu ultimo shape esta como ela explodida
    nave.shape('nave.gif')
    nave.goto(0,-200) #envia a nave para a posição original

    #ENVAI OS OBJETOS PARA UMA POSIÇÃO ALEATORIA PARA NÃO FICAR EM UMA COLISÃO INFINITA
    asteroide.goto(random.choice([-150, -100, -50, 0, 50, 100, 150]), 600) 
    asteroide2.goto(random.choice([-150, -100, -50, 0, 50, 100, 150]), 600)
    gasolina.goto(random.choice([-160, -130, -100, -70, -40, -10, 0, 30, 60, 90, 120, 150]), 0)

    Mover() #CHAMA A FUNÇÃO MOVER

    #AO PRESSIONAR A TECLA a & d NO TECLADO, IRÁ CHAMAR A FUNÇÃO
    janela.onkeypress(movimentoDireita, 'd')
    janela.onkeypress(movimentoDireita, 'D')
    janela.onkeypress(movimentoEsquerda, 'a')
    janela.onkeypress(movimentoEsquerda, 'A')
    janela.listen() #FAZ A JANELA ESCUTAR OS MOVIMENTOS DO JOGADOR

def ExplodirNave():   #FUNÇÃO PARA ANIMAR A NAVE SENDO EXPLODIDA

    nave.shape('explosion1.gif')
    janela.update()
    nave.shape('explosion2.gif')
    janela.update()
    nave.shape('explosion3.gif')
    janela.update()
    nave.shape('explosion4.gif')
    janela.update()

def colisaoJogador(): #ENCERRAR O JOGO CASO A NAVE ENCOSTE NA BORDA ESQUERDA OU DIREITA
    if nave.xcor() <= -150 or nave.xcor() >= 150:
        EncerrarJogo()

def Mover():          #FUNÇÃO GERAL QUE MOVIMENTA TODOS OS OBJETOS DO JOGO 

    #CHAMA TODAS AS FUNÇÕES
    Mecanicas_Asteroide()
    Mecanicas_Gasolina()
    AtualizarPlacar()
    colisaoJogador()

    #ATUALIZAR A TELA TODA VEZ QUE A FUNÇÃO REPETIR
    turtle.update()
    #FAZER A FUNÇÃO SER EXECUTADA DURANTE TAL INTERVALO DE TEMPO (60FPS)
    turtle.ontimer(Mover, 1000//60)

def Mecanicas_Gasolina():   #MOVIMENTOS E MECANICAS DA GASOLINA
     
    #CHAMA AS VARIAVEIS CONTADOR E GAS
    global contador
    global gas

    #CASO A GASOLINA ESTEJA DENTRO DA POSIÇÃO Y MENOR OU IGUAL A -500 (PASSE DA TELA)
    if gasolina.ycor() >= -500:
        gasolina.forward(5) #ENTAO A GASOLINA PODE SE MOVER DE 5 EM 5px
    else: #CASO ELA ESTEJA FORA DA TELA:
        #VÁ PARA UM LOCAL ALEATORIO
        gasolina.goto(random.choice([-100, -90, -70, -40, -20, -10, 0, 30, 60, 90, 100]), random.choice([600,650,700,750,800]))
    
    if gasolina.xcor() + 15 >= nave.xcor() - 15 and gasolina.xcor() - 15 <= nave.xcor() + 15 and gasolina.ycor() + 15 >= nave.ycor() - 15 and gasolina.ycor() - 15 <= nave.ycor() + 15:
        gasolina.goto(random.choice([-100, -90, -70, -40, -20, -10, 0, 30, 60, 90, 100]), random.choice([600,650,700,750,800]))
        gas += 20
        contador += 1

    #CASO A VARIAVEL GASOLINA CHEGUE A 0, O JOGO IRÁ ENCERRAR E IRÁ PRINTAR UMA MENSAGEM DE FIM DE JOGO NA TELA!
    if gas <= 0:
        EncerrarJogo()

def Mecanicas_Asteroide(): #MOVIMENTOS E MECANICAS DO ASTEROIDE

    if asteroide.ycor() >= -600: 
        asteroide.forward(10 + (distancia//2.5))    
    else:
        asteroide.goto(random.choice([-100, -80, -60, -50 -30, -10, 0, 10, 30, 50, 80, 100]), random.choice([600,650,700,750,800])) 
        
    if asteroide2.ycor() >= -600: 
        asteroide2.forward(10 + (distancia//2.5)) 
    else:
        asteroide2.goto(random.choice([-100, -80, -60, -50 -30, -10, 0, 10, 30, 50, 80, 100]), random.choice([600,650,700,750,800])) 

    if asteroide.ycor() + 30 >= nave.ycor() - 30 and asteroide.ycor() - 30 <= nave.ycor() + 30 and nave.xcor() + 30 >= asteroide.xcor() - 30 and nave.xcor() - 30 <= asteroide.xcor() + 30 :
        EncerrarJogo()
    if asteroide2.ycor() + 30 >= nave.ycor() - 30 and asteroide2.ycor() - 30 <= nave.ycor() + 30 and nave.xcor() + 30 >= asteroide2.xcor() - 30 and nave.xcor() - 30 <= asteroide2.xcor() + 30:
        EncerrarJogo()

def AtualizarPlacar():  #ALTERAR OS VALORES DO PLACAR 

    #CHAMAR AS VARIÁVEIS QUE SERÃO ALTERADAS
    global gas
    global distancia
    global pontuacao

    #TODA VEZ QUE A FUNÇÃO FOR CHAMADA
    distancia += 0.01
    gas -= 0.1
    pontuacao += 0.1
    #OS VALORES ACIMA SERÃO POSTOS

    #LOGO APÓS, LIMPARÁ O QUE O PLACAR ESCREVEU
    placar.clear()
    #E ESCREVERÁ ALGO NOVO COM AS VARIAVEIS ACIMA
    placar.write('''
GASOLINA - {:.1f}
      P1 - {:.1f}
    Km/h - {:.1f}'''.format(gas, pontuacao, distancia), font=fontePlacar)

    #MESMA COISA PARA O CONTADOR DE COCA-COLAS
    contador_placar.clear()
    contador_placar.write(f'{contador}', font=fontePlacar)

def EncerrarJogo(): #FUNÇÃO PARA ENCERRAR O JOGO (DERROTA)
    
    #CASO PERCA, A FUNÇÃO SERÁ CHAMADA E
    titulo.clear()        #LIMPARÁ O TITULO
    titulo.goto(-220,0)   #MANDARÁ O TÍTULO PARA TAL COORDENADA
    titulo.write('''
        FIM DE JOGO!
     PRESSIONE ESPAÇO!'''
,font=fonteTitulos)       #ESCREVERÁ UMA MENSAGEM DE FIM DE JOGO

    placar.clear()        #IRÁ LIMPAR O PLACAR

    contador_placar.goto(-140,-250) #IRÁ ENVIAR O CONTADOR DO PLACAR PARA TAL COORDENADA
                                    #IRÁ ESCREVER O RESULTADO DA PARTIDA (PONTUAÇÃO)
    contador_placar.write('''
    DISTANCIA: {:.1f}
    PONTUAÇÃO: {:.1f}
     COCA-COLA: {}'''.format(distancia,pontuacao, contador),font=('Courier', 15, 'bold'))
    
    ExplodirNave() #IRÁ EXPLODIR A NAVE
    #ENCERRARÁ O TURTLE
    turtle.done()

janela.listen() #FAÇA A JANELA ESCUTAR TODOS OS COMANDOS

janela.mainloop()