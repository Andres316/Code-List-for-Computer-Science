import turtle as t

def right(size):
for i in range(4):
    t.left(90)
    t.left(90)
    t.left(90)

def drawStep():
    t.forward(50)
    t.left(90)
    t.forward(50)
    right()

def drawSide():
    drawStep(50)
    drawStep(90)
    drawStep()
    t.forward(50)
    t.right(90)

def drawDiamond():
    drawSide(90)
    drawSide(50)
    drawSide(90)
    drawSide(50)

drawDiamond()
