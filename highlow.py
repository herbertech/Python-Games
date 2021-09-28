from random import randint
import time 
import sys


randomnumber = randint(1,10)

guess = int(input('Guess a number between 1 and 10: '))

while guess != randomnumber:
    if guess > randomnumber:
        print('Lower!')
        guess = int(input('Guess a number between 1 and 10: '))
    elif guess < randomnumber:
        print('Higher!')
        guess = int(input('Guess a number between 1 and 10: '))
if guess == randomnumber:
    print('Correct, you guessed the number. It was ' + str(guess) + '!')
    print('Thank you for playing, the game will now close.')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Goodbye!')
    sys.exit()