#setup info
import turtle
greg = turtle.Turtle()
greg.shape("turtle")
greg.speed(0)
greg.color

#loop for 1st (3 times) 
for i in range(3):
    greg.forward(100)
    greg.left(120)
#move turtle halfway
greg.forward(50)
greg.right(60)
#smaller triganles (half the values)
for i in range(3):
    greg.left(120)
    greg.forward(50)
