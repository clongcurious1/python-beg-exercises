#Guess the Secret Number game
#Variables
secret_number = 87
n = input('Guess the secret number between 1 and 100:\n')
n = int(n) #convert user input to whole number

#Conditional
if n == secret_number:
    print('Amazing! You guessed it.')
else:
    #not equal to secret number, check if higher or lower
    if n > secret_number:
        print('Sorry. Your guess was too high.')
    else:
        print('Sorry. Your guess was too low.')
print('Thank you for playing our guessing game.')

