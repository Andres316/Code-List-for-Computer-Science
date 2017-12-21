# calculator
print("Welcome to my calculator")
bal = 1000
interest = 0.20
years = 5

for i in range(years):
    print("Year",i,'your total balance is %.20f'% (bal))
    bal = bal*interest+bal

# initial variables, constant

INITIAL_BALANCE= 800
TARGET = INITIAL_BALANCE*3
RATE=3.0

# step 2 initialize variables used with this loop

balance = INITIAL_BALANCE
year = 0

# step 3, count the years required for the investment to triple

while balance <TARGET:
    year = year + 1
    interest = balance*RATE/100
    balance = balance + interest

# step 4, print the results

print("The investment tripled after", year, "years.")

import turtle

for i in range(1000):
    turtle.forward(i)
    turtle.right(20)
    turtle.speed(100)
