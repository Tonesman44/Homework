import turtle
greg = turtle.Turtle()
greg.speed(0)
greg.shape("turtle")


#forward, pickup, stamp, go back and turn (repeats 12 times)
for i in range(12):
    greg.penup()
    greg.forward(100)
    greg.pendown()
    greg.forward(50)
    greg.penup()
    greg.forward(25)
    greg.stamp()
    greg.backward(175) #go back to middle
    greg.right(360/12)

    

