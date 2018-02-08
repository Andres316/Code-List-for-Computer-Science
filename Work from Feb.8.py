def even(n):
    for number in range(1,n+1):
        if number % 2 == 0:
            print(number, "is even")

even(100)
    
# function that return the addition of 2 numbers

def sum_of_numbers(x,y,z):
    x=int("Enter a number")
    y=int("Enter the second number")
    z=int("Enter the third number")
    return x+y+z

print(sum_of_numbers(2,3,4))
