# this is quiz game
print("Welcome to my quiz game")
playing = input("Do want to play? ")

if playing != "yes": # if player says yes than play the game 
    quit()

print("Okay! Let's play: ")
score = 0 

answer = input("What does CPU stand for ") # this is question
if answer == "central processing unit": # if the quesion is right 
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does GPU stand for ")
if answer == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does RAM stand for ")
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


print("You got it " + str(score) + "question guesses!") # this will tell the quess
print("You got it " + str((score / 3) * 100) + "%.") # this well tell you the %
