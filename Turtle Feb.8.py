#

import turtle as t

def drawRectangle(t,w,h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

drawRectangle(t,100,50)

def drawSquare(tx,sz):
    drawnRectangle(tx,sz,sz)

drawnSquare(t,50)



