# Oregon game with functions

import random
import time

print(time.asctime())

def authenticate():
     total_triesUser=0
     total_triesPass=0
     while total_triesUser<4 and total_triesPass<4:
          theUsername=str(input("Enter your username, the press Return/Enter: "))
          if theUsername=='com':
               total_triesUser+=4
               print("Username successful")
               while total_triesPass<4:
                     thePassword=str(input("Enter the password, then press Return/Enter: "))
                     if thePassword=='127':
                          total_triesPass+=4
                          init()
                     else:
                          print("Unable to log in. ")
                          total_triesPass+=1
                          if total_triesPass>3:
                               break                         
          else:
               print("Username Incorrect.")
               total_triesUser+=1
               if total_triesUser>3:
                    break
                
import random

print("Welcome to the Oregon Trail")
print(""" You are now traveling to Oregan from New York City, Survive
and good luck.""")
print()

#variables
milesTraveled = 0
thirst = 0
Hunger = 0
Water = 30
Boredom = 0
Stink = 0
Fuel = 100
Overheated = 0
Sleepness = 0
done = False

#start main loop
while not done:
    fullSpeed = random.randrange(10, 20)
    print("""
    A. Drink from your water bottle.
    B. Ahead full speed.
    C. Stop for the night.
    D. Eat food
    E. Listen to music/watch videos
    F. Stop for Gas
    G. Let the car cool off
    H. Shower
    I. Status check
    Q. Quit.""")
    print()
    userInput = input("Your choice? ")
    if userInput.lower() == "q":
            done = True
#status
    elif userInput.lower() == "e":
        print("Miles traveled: ",milesTraveled)
        print("Bottles of water: ", Water)
        print("Your car has ", Fuel,"amount of fuel.")
        print("Your car is this hot", Overheated, "Tempature.")
        print("Your body stinks", Stink)
        print("You are getting this bored", Boredom)
        print("You are this hungry", Hunger)
        print("You are getting Sleepy", Sleepness)
#stop for the night
        elif userInput.lower() == "c":
        Sleepness *= 0
        print("You are well rested",Sleepness)
#Eating
        elif userInput.lower() == "d":
        Hunger *= 0
        print("You are not hungry",Hunger)
#Stop for gas
        elif userInput.lower() == "d":
        Fuel *= 100
        print("You are not hungry",Hunger)
#Let the car cool off
        elif userInput.lower() == "C":
        Overheated Car *= 0
        print("The car has cooled off", Overheated Car)

#drink Water Bottle
    elif userInput.lower() == "a":
    if water bottle == 0:
    print("You're out of water.")
    else:
    canteen -= 1
    thirst *= 0
    print("You have ",Water Bottle,"drinks left and you are no longer thirsty.")
    
#Take a shower
        elif userInput.lower() == "H":
        Stink *= 0
        print("You have cooled off", Stink)
#Take a break
        elif userInput.lower() == "E":
        Boredom *= 0
        print("You are not bored at all", Boredom)
    #move full speed
    elif userInput.lower() == "B":
        print("You traveled ",fullSpeed,"miles!")
        milesTraveled += fullSpeed
        thirst += 1
        Hunger+= random.randrange(1, 4)
        oasis = random.randrange(1, 21)
#not done check
    if oasis == 20:
        thirst = 0
        Hunger = 0
        Water Bottle = 30
        Boredom = 0
        Stink = 0
        Fuel = 100
        Overheated Car = 0
        Sleepness = 0
        print("You found an oasis! After taking a drink you filled your canteen and the camel is refreshed.")
    if milesTraveled >= 2,741.8 and not done:
        print("You made it across the country, you win!")
        done = True
    if thirst > 4 and thirst <= 6 and not done:
        print("You are thirsty")
    if thirst > 6:
        print("You died of dehydration!")
        done = True
    if Hunger > 5 and Hunger <= 8 and not done:
        print("You are getting hungry.")
    if Hunger > 8:
        print("You died.")
        done = True
    if Boredom > 6 and Boredom <= 9 and not done:
        print("You are going crazy")
    if Boredom > 9:
        print("You have gone mad")
    if Fuel > 50 and Fuel <= 0 and not done:
        print("You are running out of fuel")
    if Fuel > 0:
        print("Your car has ran out of fuel")
    if Overheated Car > 60 and Fuel <= 100 and not done:
        print("Your car is getting hot")
    if Overheated Car > 100:
        print("Your car blew up")
    if Sleepness > 7 and Fuel <= 10 and not done:
        print("You are getting tired")
    if Sleepness > 10:
        print("You died of tiredness")
    if Stink > 7 and Fuel <= 10 and not done:
        print("You stink")
    if Stink> 10:
        print("You died of your own smell")
               
               
