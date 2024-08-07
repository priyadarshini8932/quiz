print("Welcome to my computer quiz!")
def quit():
    print("Okay we won't play")
    exit()
    

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score =0
answer =input("What does CPU stand for? ")
if answer.lower()== "central processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 2
answer =input("What is the capital city of Australia? ")
if answer.lower()== "canberra":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 3
answer =input("Who wrote the play 'Romeo and Juliet'? ")
if answer.lower()== "william shakespeare":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 4
answer =input(" What is the chemical symbol for the element gold? ")
if answer.lower()== "au":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 5
answer =input("Which planet is known as the Red Planet? ")
if answer.lower()== "mars":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 6
answer =input("Who was the first President of the United States? ")
if answer.lower()== "george washington":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 7
answer =input(" What is the largest mammal in the world? ")
if answer.lower()== "blue whale":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 8
answer =input("Which is the longest river in the world? ")
if answer.lower()== "nile river":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 9
answer =input("Who painted the Mona Lisa? ")
if answer.lower()== "leonardo da vinci":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

# question 10
answer =input("What is the currency of Japan?")
if answer.lower()== "yen":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

print("You got "+ str(score)+"questions correct!")
print("You got "+ str((score/10)*100)+"%")

