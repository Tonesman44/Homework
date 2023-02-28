import turtle
t = turtle.Turtle()
def drawNgon(t, numSides, sideLength):
    for i in range(numSides):
        t.forward(sideLength)
        t.left(360/numSides)
drawNgon(t, 3, 50)
#This function takes in a turtle object t, an integer numSides, and a float sideLength.
#It uses the turtle to draw a polygon with numSides sides,
#with each side of length sideLength.
    
