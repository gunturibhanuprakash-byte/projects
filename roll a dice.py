## loop
#   ask: roll the dice(y/n)
#   if user enters y
#       generate two random numbers
#       print them
#   elif user enters n
#       print thankyou for playing
#       terminate
#   else 
#       print invalid choice
import random
while True:
    choice=input('do you want to roll the dice (y/n) : ').lower()
    if choice == 'y' :
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'{dice1},{dice2}')
    elif choice == 'n':
        print("thankyou for playing")
        break
    else :
        print("entered invalid choice")
