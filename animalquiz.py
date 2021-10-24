#packages - notes that are also included in Readme
#imports
#functions
#functions
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer. You earn 1 point.')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong anser. Try again: ')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct answer is ' + answer)
#variables
score = 0
#mainprogram
print('***GUESS THE ANIMAL***\n')
print('For each question, you can enter up to 3 guesses.\n')
#question 1
guess1 = input('Which bear lives at the North Pole? 2 word answer: ')
#check the answer by CALLING the function
check_guess(guess1, 'polar bear')
#question 2
guess2 = input('\nWhat is the fastest land animal? 1 word answer: ')
#CALL the function to check the answer
check_guess(guess2, 'cheetah')
#question 3
guess3 = input('\nWhat is the largest animal on land or in the sea? 1 word answer: ')
#CALL the function to check the answer
check_guess(guess3, 'whale')
#display score
print('\nYour score is: ', str(score))
print('Thank you for playing our guessing game.')