# Trivia quiz

print("This is a quiz that test your knowledge on ___")

'''
'''

name= input("Enter your name: ")
print("Hi, there,", name, "Are you ready to start the quiz?")

print("I will ask you 6 questions and give you three choices")
print("Select which choice is the correct answer, a, b or c")

# set the score of the quiz to 0
score = 0
score = int(score)

# question 1
print("Question 1: Who is the richest superhero? \n")

print('a.Batman')
print("b.Iron Man")
print("c.Black Panther")

Q1answer="c" # the right answer to question 1
Q1response= input("Your answer: ")

if Q1response == "C" or Q1answer== 'c':
    print("Correct answer", Q1answer)
    score= score+1

elif Q1response != "B" and Q1response != 'b' :
    print("Sorry, incorrect")
    score= score-1
print("Your current score is ",score, "out of 6")

# percentage score

final_score = (score*100)/6
print("This is a score of " +str(final_score)+ " percent")

# question 2
print("Question 2: Who is the first Green Lantern\n")

print('a.Alan Scott')
print("b.Hal Jordan")
print("c.Guy Gardner")

Q2answer="a" # the right answer to question 2
Q2response= input("Your answer: ")

if Q2response == "A" or Q2answer== 'a':
    print("Correct answer", Q1answer)
    score= score+1

elif Q2response != "B" and Q2response != 'b' :
    print("Sorry, incorrect")
    score= score-1
print("Your current score is ",score, "out of 6")

# percentage score

final_score = (score*100)/6
print("This is a score of " +str(final_score)+ " percent")

# question 3
print("Question 2: When did Superman die\n")

print('a.2000')
print("b.1995")
print("c.1992")

Q3answer="c" # the right answer to question 3
Q3response= input("Your answer: ")

if Q3response == "C" or Q3answer== 'c':
    print("Correct answer", Q1answer)
    score= score+1

elif Q3response != "B" and Q3response != 'b' :
    print("Sorry, incorrect")
    score= score-1
print("Your current score is ",score, "out of 6")

# percentage score

final_score = (score*100)/6
print("This is a score of " +str(final_score)+ " percent")
