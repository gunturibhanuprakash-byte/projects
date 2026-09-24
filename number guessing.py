#number to be guessed= random number between 1 to 100
## loop
#   ask: guess the number from 1 to 100:
#   if guess > number to be guessed
#       print: guess is too high
#   elif guess < number to be guessed
#       print : guess is too low
#   else:
#       print: congratulations you guessed the number
#       terminate
import random


num_to_be_guessed = random.randint(1,100)

while True:
    try:
        guess= int(input('guess the number from 1 to 100 :'))
        if guess > num_to_be_guessed:
            print('too high')
        elif guess <num_to_be_guessed:
            print('too low')
        else:
            print('congratulations you guessed the number')
            break
    except ValueError:
            
        print('please enter a valid number')