# Calculator

import math
import random
from math import sqrt

def welcome():
    menu=input('''Welcome to ...Press 1 for basic operation
Press 2 for more advanced math operations

''')
    if menu =='1':
        calculate_basic()
    elif menu=='2':
        calculate_adv()

def calculate_basic()
    operation= input('''
Please type the math operation you want to complete
+ for addition
- for subtraction
* for multiplication
% for modulus
/regular division
// integer division
''')

firstNumber=float(input("Please enter the first number"))
secondNumber=float(input("Please enter the second number"))

if operation =='+':
    print('{}+{}='.format(firstNumber, secondNumber))
    print(firstNumber+secondNumber)
elif operation == '-':
    print()
    print()

    else:
        print("You have not typed a valid operator. Run the program again')
    runAgain()

def
