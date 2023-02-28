import turtle
t = turtle.Turtle()
t.speed(0)
def drawNgonSpiral(t, numSides, sideLength, numShapes):
    for i in range(numShapes): #Turn a degree before you make that shape again
        t.left(360/numShapes)
        for i in range(numSides): #makes one shape
            t.fd(sideLength)
            t.left(360/numSides)
drawNgonSpiral(t, 6, 100, 35)
#Calls the number of sides 6, length 100, and number of shapes 35)


