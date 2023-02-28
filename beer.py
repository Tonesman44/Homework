#Creates a function and loops it
def beer(n):
    for i in range(n): 
        print (n, "bottles of beer on the wall", n, "bottles of beer. Take one down, pass it around,", n-1, "bottles of beer on the wall")
        n = n - 1
#Prints response where n is then subtracts it by 1, then repeats each time
n = int(input("How many bottles of beer are on the wall?"))
beer(n)
        
