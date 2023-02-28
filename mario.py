def mario(height):
    for i in range(1, height +1, 1):
        print("")
        for dots in range(height - i, 0, -1):
            print(".", end = "")
        for i in range(i):
            print("#", end = "" )

#Prmopts user and if greater than 8 or less than 1 then it will ask user again
height = int(input("How tall should the pyramid be?"))
while height < 1 or height > 8:
    height = int(input("How tall should the pyramid be?"))

mario(height)
