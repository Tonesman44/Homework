#Defines function, uses for loop to calculate sum of all numbers squared from 1 to n
def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    print(result)

#Get input and make into int, call function
n = int(input("Sum of squares with which number? " ))
sum_of_squares(n)

