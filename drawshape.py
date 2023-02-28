import turtle
greg = turtle.Turtle()
greg.speed(0)
greg.shape("turtle")

n = int(input("How many sides are there: "))
for i in range(n):
        greg.forward(50)
        greg.left(360/n)
#Asks user for sides then drawns (a circle divided by the amount of sides) = degrees of that shape
        
