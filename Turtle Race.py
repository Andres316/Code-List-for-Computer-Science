#Turtle Race
from turtle import *
from random import randint
'''
write(0)
forward(100)
write(5)
'''
'''
write(0)
forward(20)

write(1)
forward(20)

write(2)
forward(20)

write(3)
forward(20)

write(4)
forward(20)

write(5)
forward(20)

penup()
'''
speed(10)
penup()
goto(-140,140)
for step in range(10):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

Raph=Turtle()
Raph.color('red')
Raph.shape('turtle')

Raph.penup()
Raph.goto(-160,100)
Raph.pendown()

Leo=Turtle()
Leo.color('blue')
Leo.shape('turtle')

Leo.penup()
Leo.goto(-160,80)
Leo.pendown()

Mikey=Turtle()
Mikey.color('orange')
Mikey.shape('turtle')

Mikey.penup()
Mikey.goto(-160,60)
Mikey.pendown()


Donnie=Turtle()
Donnie.color('purple')
Donnie.shape('turtle')
    
Donnie.penup()
Donnie.goto(-160,40)
Donnie.pendown()

for turn in range(100):
    Raph.forward(randint(1,5))
    Leo.forward(randint(1,5))
    Mikey.forward(randint(1,5))
    Donnie.forward(randint(1,5))
