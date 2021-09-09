import random
roll = random.randint(1,6)
guess = int(input('Guess what number the computer rolled. Choose number between 1 and 6.3\n'))

if guess == roll:
    print('Correct! The computer rolled a ' + str(roll))
else:
    print('Wrong! The computer rolled a ' + str(roll))