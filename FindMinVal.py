# make a function that searches through a list

import random

#define some list

section12A= [80,75,88,80,90,77,65]
section12B= [80,75,88,80,90,77,65]
section12C= [80,75,88,80,90,77,65]
section12D= [80,75,88,80,90,77,65]


def minVal(myList):
    print("Original values: ",  myList)
    minVal =100
    for i in range(len(myList)):
        if myList[i] < minVal:
           minVal = myList[i]
        print("The smallest value in the list is", minVal)

findMinVal(section12A)
findMinVal(section12B)
findMinVal(section12C)
findMinVal(section12D)

