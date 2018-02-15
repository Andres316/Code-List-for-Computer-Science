
import turtle
import random

for i in range(2):
    random_num1= random.randint(1,7)
    random_num2= random.ranint(1,7)
    print(random_num1)
    print(random_num2)

def square(size):
     for i in range(4):
         turtle.forward(size)
         turtle.right(90)

square(random.randint(10,100))

'''
def square(size):
     for i in range(4):
         turtle.forward(size)
         turtle.right(90)
