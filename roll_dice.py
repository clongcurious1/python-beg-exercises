import random
roll = random.randint(1,6)
guess = int(input("Guess what number the computer rolled?\n"))

if guess == roll:
    print ("Correct! The computer rolled a" + " " + str(roll))
else:
    print("Wrong! The computer rolled a" + " " + str(roll))


