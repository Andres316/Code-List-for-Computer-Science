# write a program that returns random choices to the user
import random

def getAnswer(answerNumber):
    if answerNumber==1:
        return "NYU"
    elif answerNumber==2:
        return "Harvard"
    elif answerNumber==3:
        return "Syracuse"
    elif answerNumber==4:
        return "Hamburger University"
    elif answerNumber==5:
        return "Held Back"
    elif answerNumber==6:
        return "Pace University"
    elif answerNumber==7:
        return "Yale"
    elif answerNumber==8:
        return "St.John"
    elif answerNumber==19:
        return "BMCC"

tries= 0

while tries<5:
    userInput= input("What college will I go to: ")
    if userInput=='1':
        print(getAnswer(random.randint(1,9)))
        tries = tries+1
    elif userInput=='2':
        print(getAnswer(random.randint(1,9)))
        tries= tries+1
    if tries==3:
        break
