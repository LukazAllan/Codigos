# PT-BR
# Ping Pong usando Python 3.8.1
# Criado por Allan Lucas
# EN-US
# Pong using Python 3.8.1
# Created by Allan Lucas
from time import sleep as slp
import turtle
"""
:param ecra: Gera a tela
"""


class Sub:
    """docstring for Sub"""

    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print(f'{self.name} recebeu msg {msg}')


class Pub:
    """docstring for Pub"""

    def __init__(self):
        self.subs = set()

    def reg(self, who):
        self.subs.add(who)

    def can(self, who):
        self.subs.discard(who)

    def note(self, msg):
        print(f'Notifying {len(self.subs)} observers')
        for sub in self.subs:
            sub.update(msg)


altura_p1: int = 5
altura_p2 = 5

# Tela
ecra = turtle.Screen()
ecra.title("Ping-Pong")
ecra.bgcolor("black")
ecra.setup(width=800, height=600)
ecra.tracer(0)

# Pontuacao
pt_p1 = 0
pt_p2 = 0

# p1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape('square')
p1.color("white")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350, 0)

# p2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape('square')
p2.color("white")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350, 0)

# bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.25
bola.dy = 0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('P1: 0   P2: 0', align='center', font=("Montserrat", 24, "normal"))


# Funcoes
def p1_up():
    y = p1.ycor()
    y += 20
    p1.sety(y)


def p1_down():
    y = p1.ycor()
    y -= 20
    p1.sety(y)


def p1_right():
    x = p1.xcor()
    x += 20
    p1.setx(x)


def p1_left():
    x = p1.xcor()
    x -= 20
    p1.setx(x)


def p2_up():
    y = p2.ycor()
    y += 20
    p2.sety(y)


def p2_down():
    y = p2.ycor()
    y -= 20
    p2.sety(y)


# Cracks
def bola_acel():
    bola.dx *= 1.25
    bola.dy *= 1.25


def bola_ret():
    bola.dx /= 1.25
    bola.dy /= 1.25


def aumentar_p1():
    global altura_p1
    altura_p1 += 1
    p1.shapesize(stretch_wid=altura_p1, stretch_len=1)


def normal():
    bola.dx = 0.25
    bola.dy = 0.25


def celto():
    print('celto')


# keyboard binding
ecra.listen()
ecra.onkey(p1_up, "w")
ecra.onkey(p1_down, "s")
ecra.onkey(p1_left, "a")
ecra.onkey(p1_right, "d")
ecra.onkey(p2_up, "i")
ecra.onkey(p2_down, "k")
ecra.onkeypress(bola_acel, "o")
ecra.onkeypress(bola_ret, "p")
ecra.onkeypress(normal, "n")
ecra.onkeypress(aumentar_p1, "1")

# Main game loop
while True:
    ecra.update()
    print(type(int(p1.xcor())))

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Deteccao de borda
    if bola.ycor() > 290:  # Topo
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:  # Baixo
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:  # Esquerda
        bola.goto(0, 0)
        bola.dx *= -1
        pt_p1 += 1
        pen.clear()
        pen.write(f'CPU: {pt_p1 + pt_p2}', align='center', font=("Montserrat", 24, "normal"))

    if bola.xcor() < -390:  # Direita
        bola.goto(0, 0)
        bola.dx *= -1
        pt_p2 += 1
        pen.clear()
        pen.write(f'CPU: {pt_p1 + pt_p2}', align='center', font=("Montserrat", 24, "normal"))

    # Colisoes entre Raquete e Bola
    if (340 < bola.xcor() < 350) and (
            p2.ycor() + (altura_p2 * 10 + 2) > bola.ycor() > p2.ycor() - (altura_p2 * 10 + 2)):
        bola.setx(340)
        bola.dx *= -1

    if ((int(p1.xcor())+10) > bola.xcor() > int(p1.xcor())) and (
            p1.ycor() + (altura_p1 * 10 + 2) > bola.ycor() > p1.ycor() - (altura_p1 * 10 + 2)):
        bola.setx(-340)
        bola.dx *= -1
