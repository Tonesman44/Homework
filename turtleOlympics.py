#Naming and importing the turtle
import turtle
greg = turtle.Turtle()
greg.shape("turtle")
greg.color("blue")
greg.speed(5)
greg.pensize(3)


#equation for circumferance
pi = 3.1415
radius = 50
circf = 2*pi*radius

#Function for defining a circle
def circle():
    for _ in range (40):
        greg.forward(circf/40)
        greg.left(360/40)

#First circle
circle()
r = 0
f = 0

#Draws circle then picks up and moves and repeats
for i in range(2):
    greg.penup()
    greg.right(r + 45)
    greg.forward(45 - f)
    greg.pendown()
    circle()

    greg.left(60)
    greg.penup()
    greg.forward(115)
    greg.pendown()
    circle()
#adjusts angle on the last circle
    r += 20
    f += 10

