# Trivia quiz

print("This is a quiz that test your knowledge on ___")

'''
'''

name= input("Enter your name: ")
print("Hi, there,", name, "Are you ready to start the quiz?")

print("I will ask you 6 questions and give you three choices")
print("Select which choice is the correct answer, 1, 2 or 3")

# set the score of the quiz to 0
score = 0
score = int(score)

# question 1
print("Question 1: Who is the richest superhero? \n")

print('1.Batman')
print("2.Iron Man")
print("3.Black Panther")

Q1answer="3" # the right answer to question 1
Q1response= input("Your answer: ")

if Q1response =="3" or Q1answer== '3':
    print("Correct answer", Q1answer)
    score= score+1
elif Q1response != "B" or Q1response != 'b':
    print("Sorry, incorrect")

print("Your current score is ",score, "out of 6")

# percentage score

final_Score = (score*100)/6
print("This is a score of " +str(final_score)+ " percent")

