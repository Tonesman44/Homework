#setup
import turtle
t = turtle.Turtle()
t.speed(0)
t.shape("turtle")
t.color("green")
#no input functions
def drawSquare(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)
#drawSquare(t, 50)
#turtle, size of one square

def drawRow(t, length, size):
    for i in range(length):
        drawSquare(t, size)
        t.forward(size)
#drawRow(t, 5, 50)
#turtle, how many squares, size of each

def drawGrid(t, grid, size):
    for i in range(grid):
        drawRow(t, grid, size)
        t.penup()
        t.goto(0,0)
        t.right(90)
        t.forward((size*i)+size)
        t.left(90)
        t.pendown()
#drawGrid(t, 5, 50)
#turtle, amount of squares, size of each

def drawSquareStairs(t, height, size):
    for i in range(height):
        drawRow(t, i+1, size)
        t.penup()
        t.goto(0,0)
        t.right(90)
        t.forward((size*i)+size)
        t.left(90)
        t.pendown()
   
drawSquareStairs(t, 5, 50)
#turtle, height of stairs, size of each square
    
    
    

