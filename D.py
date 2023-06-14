
import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen() #Crea una ventana gráfica para el juego.
wn.title("Joc de la Serp per Eric Simo") #Establece el título de la ventana del juego.
wn.bgcolor("green") #Establece el color de fondo de la ventana en verde.
wn.setup(width=600, height=600) #Establece el tamaño de la ventana en 600x600 píxeles.
wn.tracer(0) # Desactiva las actualizaciones automáticas de la ventana. Al no actualizarse se ira acumulando la velocidad de la serpiente.

# Snake head
head = turtle.Turtle() #Crea el objeto head de la clase Turtle, que representa la cabeza de la serpiente.
head.speed(0) # Establece la velocidad de animación de la cabeza en la máxima.
head.shape("square") # Establece la forma de la cabeza como un cuadrado.
head.color("black") # Establece el color de la cabeza en negro.
head.penup() # Levanta el lápiz para evitar que se dibuje una línea mientras la cabeza se mueve.
head.goto(0,0) #  Mueve la cabeza a la posición inicial en las coordenadas (0, 0).
head.direction = "stop" # Establece la dirección inicial de la cabeza como "stop" (sin movimiento).

# Snake food
food = turtle.Turtle() # Crea el objeto food de la clase Turtle, que representa la comida para la serpiente.
food.speed(0) # Establece la velocidad de animación de la comida en la máxima.
food.shape("circle") # Establece la forma de la comida como un círculo.
food.color("red") # Establece el color de la comida en rojo.
food.penup() # Levanta el lápiz para evitar que se dibuje una línea mientras la comida se mueve.
food.goto(0,100) # Mueve la comida a una posición inicial aleatoria en el eje y.

segments = [] # Crea una lista vacía para almacenar los segmentos del cuerpo de la serpiente.

# Pen
pen = turtle.Turtle() # Crea el objeto pen de la clase Turtle, que se utiliza para mostrar la puntuación en la ventana.
pen.speed(0) # Establece la velocidad de animación del lápiz en la máxima.
pen.shape("square") # Establece la forma del lápiz como un cuadrado.
pen.color("white") # Establece el color del lápiz en blanco.
pen.penup() # Levanta el lápiz para evitar que se dibuje una línea mientras el lápiz se mueve.
pen.hideturtle() # Oculta la forma del lápiz.
pen.goto(0, 260) #Mueve el lápiz a la posición donde se mostrará la puntuación.
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal")) #Escribe la puntuación inicial en la ventana.

# 49-66: Definición de funciones de control de dirección (go_up, go_down, go_left, go_right) y función de movimiento (move).
# wn.listen(): Escucha los eventos de teclado en la ventana.

# Functions
def go_up(): 
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
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

# wn.onkeypress(go_up, "w"): Asocia la tecla "w" con la función go_up.

# wn.onkeypress(go_down, "s"): Asocia la tecla "s" con la función go_down.

# wn.onkeypress(go_left, "a"): Asocia la tecla "a" con la función go_left.

# wn.onkeypress(go_right, "d"): Asocia la tecla "d" con la función go_right.

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Ara es crea un Loop del Joc perque no acabi mai
while True:
    wn.update()

    # Mira que si el cap de la serp colisona que torni a començar
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Revisa ses colisions amb sa fruita de la serp
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Revisa que si el cap de la serp choca amb el cos es reinici
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()