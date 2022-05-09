import random # this module 

top_of_range = input("Type a number: ") # entry the rates of numbers

if top_of_range.isdigit(): # this integer
    top_of_range = int(top_of_range) 

    if top_of_range <= 0: # entry above zero
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
random_number = random.randint(0, top_of_range)
guesses = 0

while True: # loop
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit(): # this is integer
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it", guesses, "guesses!")