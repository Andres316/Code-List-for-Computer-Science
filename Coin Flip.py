# simulate a coin flip 10 times

import random

# track the number of simulations
# 1= head, 0= tails

simNum = 0
flip = random.randint(0,1)
countHeads = 0

while countHeads<5:
    flip=random.randint(0,1)
    if flip==1:
           countHeads= countHeads+flip
    print(flip)
    print("Heads =", countHeads)
    simNum  =simNum + 1

print("Total flips:",simNum)
