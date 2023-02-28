#first loop (i) is colunm
#second loop (j) is individual rows
# Multiply i * j, 1 x 1, then keeps going until the input ends
def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end='\t') #Increases the indent
        print()
#Stops the row
        
#Takes input and makes it into an int
n = int(input("What number do you want to display a multiplication table of: "))
multiplication_table(n)
