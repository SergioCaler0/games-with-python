import turtle
import time
import random

retrasar = 0.1 # retrasamos el movimiento de la serpiente
window = turtle.Screen()

#Marcador
score = 0
high_score = 0

# Name of the window
window.title("Snake")

# background color
window.bgcolor("black")

# resize window
window.setup(width= 600, height= 600)
window.tracer(0)

# head snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("pink")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food.direction = "stop"

# snake body

segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0               High Score: 0", align= "center", font=("Courier", 24, "normal"))
#functions
def snakeup():
    head.direction = "up"
def snakedown():
    head.direction = "down"
def snakeleft():
    head.direction = "left"
def snakeright():
    head.direction = "right"

def movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard

window.listen()
window.onkeypress(snakeup, "Up")
window.onkeypress(snakedown, "Down")
window.onkeypress(snakeleft, "Left")
window.onkeypress(snakeright, "Right")


while True:
    window.update()

    #colisiones bordes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Esconder segmentos
        for segmento in segmentos:
            segmento.goto(1000, 1000)
        
        segmentos.clear()


    # colisiones de la comida
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segmento = turtle.Turtle()
        new_segmento.speed(0)
        new_segmento.shape("square")
        new_segmento.color("pink")
        new_segmento.penup()
        segmentos.append(new_segmento)

        #Aumentar marcador
        score += 10

        if score > high_score:
            high_score = score
        texto.clear()
        texto.write(f"Score: {score}               High Score: {high_score}", align= "center", font=("Courier", 24, "normal"))

# move body snake
    total_segmento = len(segmentos)
    for index in range(total_segmento -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if total_segmento > 0:
        x = head.xcor()
        y = head.ycor()
        segmentos[0].goto(x,y)
    
        


    movement()
    time.sleep(retrasar)
