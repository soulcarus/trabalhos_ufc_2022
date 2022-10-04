# João Ícaro Moreira Loiola
# Matrícula: 537176

import turtle  # importa biblioteca turtle
import random  # importa modulo random


# parar de lagar e definir os FPS do game

def lag():
    janela.ontimer(lag, 1000 // 30)

# CRIA OS GIFS QUE REPRESENTAM AS IMAGENS DOS OBJETOS:

gif = 'maçã.gif'
gif1 = 'veneno.gif'
gif2 = 'coração.gif'

# CRIA JANELA DO JOGO

janela = turtle.Screen()
janela.setup(width=1000, height=1000)
janela.title('Hollow Turtle')

# ADICIONA OS GIFS NO GAME:

janela.addshape(gif)  # adiciona o shape do personagem principal
janela.addshape(gif1)  # adiciona o shape do veneno
janela.addshape(gif2)  # adiciona o shape do coração

# ATRIBUTOS DO PINCEL QUE DESENHA A ARENA:

personagem = turtle.Turtle()  # cria personagem
personagem.hideturtle()  # esconde personagem
personagem.pen(pencolor='sienna', pensize=10, speed=0)  # determina a cor, o tamanho e a velocidade do personagem
personagem.penup()  # para de riscar
personagem.goto(0, -400)  # move o personagem até as coordenadas x y
personagem.pendown()  # começa a riscar

# FORMAR A ARENA:

for i in range(4):  # repete os movimentos a seguir 4x, criando um quadrado ( arena )
    personagem.forward(400)
    personagem.left(90)
    personagem.forward(400)

#esconde a tartaruga

personagem.hideturtle()

# CRIAR JOGADOR PRINCIPAL:

boneco = turtle.Turtle()  # cria boneco
boneco.speed(2)
boneco.left(90)
boneco.shape('turtle')  # cria formato do boneco
boneco.color('purple')  # define cor do boneco
boneco.shapesize(3)  # define tamanho do boneco
boneco.penup()  # para de riscar

# MOVIMENTAÇÃO DO JOGADOR:

def bonecodireita():  # cria uma função bonecodireita
    boneco.right(5)


def bonecoesquerda():
    boneco.left(5)


def bonecocima():
    boneco.forward(10)


def bonecodesce():
    boneco.back(10)


# CONFIGURAÇÕES DO TECLADO PARA JOGADOR

janela.onkeypress(bonecocima, "w")  # ao pressionar tecla w, retorna a função bonecocima, que faz ele subir
janela.onkeypress(bonecodesce, "s")  # ao pressionar tecla s, retorna a função bonecodesce, que o faz descer
janela.onkeypress(bonecoesquerda, "a")  # ao pressionar tecla a, retorna a função bonecoesquerda, que o faz ir a esquerda
janela.onkeypress(bonecodireita, "d")  # ao pressionar tecla d, retorna a função bonecodireita, que o faz ir a direita
janela.listen()  # faz a janela escutar

# CRIAR O VENENO (CONTRA-OBJETIVO DO JOGO)

veneno = turtle.Turtle()  # cria objeto veneno
veneno.speed(5)  # define a velocidade do veneno
veneno.shape(gif1)  # define o formato do veneno
veneno.penup()  # faz parar de riscar
veneno.goto(random.randint(-370, 370), random.randint(-370, 370))  # envia veneno para tal coordenada aleatoria

# CRIAR FRUTA (OBJETIVO DO JOGO)

comida = turtle.Turtle()  # define comida
comida.shape(gif)  # define o formato da comida
comida.speed(5)  # define a velocidade
comida.penup()  # faz parar de riscar
comida.goto(random.randint(-370, 370), random.randint(-370, 370))  # faz ir para essa coordenada aleatoria

# VIDA1:

vida1 = turtle.Turtle()  # cria vida 1
vida1.hideturtle()  # esconde vida
vida1.penup()  # para de riscar
vida1.speed(0)  # define velocidade
vida1.shape(gif2)  # define formato
vida1.goto(-380, 440)  # define coordenada de spawn
vida1.showturtle()  # mostra vida

# VIDA2:

vida2 = turtle.Turtle()  # cria outra vida
vida2.hideturtle()  # faz ela desaparecer
vida2.penup()  # parar de riscar
vida2.shape(gif2)  # define seu formato
vida2.speed(0)  # define sua velocidade
vida2.goto(-300, 440)  # define sua posição
vida2.showturtle()  # faz aparecer novamente

# vida3

vida3 = turtle.Turtle()  # cria vida 3
vida3.hideturtle()  # faz desaparecer
vida3.penup()  # parar de riscar
vida3.shape(gif2)  # define seu formato
vida3.speed(0)  # define sua velocidade
vida3.goto(-220, 440)  # define sua posição inicial
vida3.showturtle()  # faz aparecer novamente

# PLACAR DE PONTOS:

placar = turtle.Turtle()  # cria placar dos pontos
placar.hideturtle()  # esconde placar
placar.speed(0)  # define sua velocidade
placar.color('deep sky blue')  # define sua cor
placar.penup()  # faz ele parar de riscar
placar.goto(60, 410)  # faz ele aparecer nessa posição
placar.write('Pontuação: ',
             font=('Calibri', 30, 'normal'))  # faz ele escrever a palavra PONTUAÇÃO com font CALIBRI e tamanho 30

# CRIAR NUMERACAO DO PLACAR:

i = 0  # valor inicial dos pontos
pontos = turtle.Turtle()  # crio o numero dos pontos
pontos.speed(0)  # define sua velocidade
pontos.penup()  # faz ele parar de riscar
pontos.goto(280, 410)  # faz ele aparecer nessa posição
pontos.pencolor('black')  # definir a cor
pontos.write(f'{i}', align='center',
             font=('Calibri', 30, 'normal'))  # faz ele escrever a o numero {i} com font CALIBRI e tamanho 30
pontos.hideturtle()  # esconde a tartaruga

# colisoes dano e pontuação:

while veneno and comida:
    veneno.forward(5)  # enquanto eles estiverem se movendo
    comida.forward(5)  # enquanto eles estiverem se movendo

    if veneno.xcor() >= 380:  # SE A POSIÇÃO X DO VENENO PASSAR DE 380, ELE IRÁ PARAR, E IRÁ VIRAR PARA LEFT COM UM NUMERO ALEATÓRIO
        veneno.speed(0)  # veneno recebe velocidade 0
        veneno.setpos(380,
                      veneno.ycor())  # define a posiçao do veneno para a mesma( x = 380) e para o y qualquer, também a mesma
        veneno.left(random.randint(0, 320))  # faz ele virar para esquerda em um valor aleatório entre 0 e 360

    elif veneno.xcor() <= -380:
        veneno.speed(0)
        veneno.setpos(-380, veneno.ycor())
        veneno.left(random.randint(0, 320))

    elif veneno.ycor() >= 380:
        veneno.speed(0)
        veneno.setpos(veneno.xcor(), 380)
        veneno.left(random.randint(0, 320))

    elif veneno.ycor() <= -380:
        veneno.speed(0)
        veneno.setpos(veneno.xcor(), -380)
        veneno.left(random.randint(0, 320))

    if comida.xcor() >= 380:
        comida.speed(0)
        comida.setpos(380, comida.ycor())
        comida.left(random.randint(0, 320))

    if comida.xcor() <= -380:
        comida.speed(0)
        comida.setpos(-380, comida.ycor())
        comida.left(random.randint(0, 320))

    if comida.ycor() >= 380:
        comida.speed(0)
        comida.setpos(comida.xcor(), 380)
        comida.left(random.randint(0, 320))

    if comida.ycor() <= -380:
        comida.speed(0)
        comida.setpos(comida.xcor(), -380)
        comida.left(random.randint(0, 320))

    # COLISÃO DO BONECO

    if boneco.xcor() >= 380:  # se a coordenada x do boneco for igual ou maior que 380...
        boneco.setpos(379, boneco.ycor())  # voltará um pixel de segurança

    if boneco.xcor() <= -380:
        boneco.speed(0)
        boneco.setpos(-379, boneco.ycor())

    if boneco.ycor() >= 380:
        boneco.speed(0)
        boneco.setpos(boneco.xcor(), 379)

    if boneco.ycor() <= -380:
        boneco.speed(0)
        boneco.setpos(boneco.xcor(), -379)

    # DIMINUIR VIDA AO COLIDIR COM O VENENO:

    if boneco.distance(
            veneno) <= 50 and vida1.isvisible() == True:  # se a distancia do veneno for menor ou igual a 50 e a vida 1 estiver visível...
        vida1.hideturtle()  # esconderemos a vida 1
        veneno.goto(random.randint(-370, 370),
                    random.randint(-370, 370))  # o veneno irá reaparecer em uma coordenada aleatória

    if boneco.distance(veneno) <= 50 and vida2.isvisible() == True:
        vida2.hideturtle()
        veneno.goto(random.randint(-360, 360), random.randint(-360, 360))

    if boneco.distance(veneno) <= 50 and vida3.isvisible() == True:
        vida3.hideturtle()
        turtle.bye()  # caso as 3 imagens tenham de sumir, o turtle irá encerrar.

    # GANHAR PONTOS AO COLETAR COMIDA:

    if boneco.distance(
            comida) <= 50:  # se a distancia entre o boneco e a comida for menor ou igual a 50 px ( tamanho da imagem )
        pontos.clear()  # limparemos os pontos
        i += 1  # o valor i aumentará em 1
        pontos.goto(280, 410)  # os pontos voltarão para o local anterior
        pontos.write(f'{i}', align='center',
                     font=('Calibri', 30, 'normal'))  # escreverão igual anteriormente, com um novo valor i
        comida.speed(0)  # definiremos a velocidade da comida como 0
        comida.goto(random.randint(-370, 370),
                    random.randint(-370, 370))  # assim ela vai imediatamente para um local aleatório e andará

janela.mainloop()
