#A simple numbers guessing game. The game will generate a random number between 0 and 20.
#The user will be told if their guess is correct, too low, or too high.
#The user has 3 guesses. Once they use up the 3 guesses, the game is over and the number is revealed.
import random
randInt = random.randint(0,20)
# print(randInt)



i = 3
while 1<=i<=3: #once i<1, command line returns to base
    guess = int(input("Guess the number "))
    if guess == randInt:
        print("Your guess was " + str(guess) + "..." + "This is correct!")
    elif guess > randInt:
        print("Your guess was " + str(guess) + "..." + "This is too high; try again")
        i-=1
        print("Turns left: " + str(i))
    elif guess < randInt:
        print("Your guess was " + str(guess) + "..." + "This is too low; try again")
        i-=1
        print("Turns left: " + str(i))

if i<1:
    print("Game over. You're out of turns. The correct answer was " + str(randInt) + ".")
