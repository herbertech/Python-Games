from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from random import randint
import os
options = Options()
#Firefox starts in headless mode, no UI shows
options.headless = True
browser = webdriver.Firefox(options=options)
#Monitor the number of errors the player made.
errorCount = 0
#These are the body parts and items for the gallow.
top = ['    ', '________']
cord = ['    ', '       |']
head = ['    ', '       |']
body = ['  ', ' ', ' ', ' ', '      |']
legs = ['  ', ' ', ' ',' ', '      |']
base = ['   ________|']
# Grab some words from a randomwords website and throw them into a list.
wordList = []
def scrapeWords(url):
    browser.get(url)
    #for loop that runs 12 times, grabbing the nth generated word via CSS selector.
    for i in range(1,13):
        elem = browser.find_element_by_css_selector('.Rand-stage > ol:nth-child(1) > li:nth-child(%s) > span:nth-child(1)' % str(i))
        wordList.append(elem.get_attribute('innerHTML'))
scrapeWords('https://www.randomlists.com/random-words')

#Function to ask player to play again.

def playAgain():
    #variables for the original state of the gallow
    top_original = ['    ', '________']
    cord_original = ['    ', '       |']
    head_original = ['    ', '       |']
    body_original = ['  ', ' ', ' ', ' ', '      |']
    legs_original = ['  ', ' ', ' ',' ', '      |']
    base_original = ['   ________|']
    global errorCount, cord, head, body, legs
    replay = ()
    while replay != 'y' or replay != 'yes' or replay != 'n' or replay != 'no':
        replay = input('Do you want to play again? enter y(es) or n(o) : ')
        if replay == 'y' or replay == 'yes':
            print("Let's play again!\n\n")
            errorCount = 0
            cord = cord_original #set the gallow back to original state
            head = head_original
            body = body_original
            legs = legs_original
            hangMan()
            break
        if replay == 'n' or replay == 'no':
            browser.close()
            os.remove('geckodriver.log')
            exit()
        elif replay != 'y' or replay != 'yes' or replay != 'n' or replay != 'no':
            print('Please answer y(es) or n(o)')

#Function that prints out the hangman as it is at that time.

def printHangman():
    #prints the gallow/hangman by joining the lists together
    print(''.join(top))
    print(''.join(cord))
    print(''.join(head))
    print(''.join(body))
    print(''.join(legs))
    print(''.join(base))
def addPart():
    if errorCount == 1:
        cord[0] = ('   |') #adds the cord
    if errorCount == 2:
        head[0] = ('   o') #adds the head
    if errorCount == 3:
        body[2] = ('|') #adds torso
    if errorCount == 4:
        body[1] = ('-') #adds left arm
    if errorCount == 5:
        body[3] = ('-') #adds right arm
    if errorCount == 6:
        legs[1] = ('/') #adds left leg
    if errorCount == 7:
        legs[3] = ('\\') #adds right leg

#Main function, where most of the magic happens.
def hangMan():
    #defining the local variables for this function

    #gets a random word from the list grabbed by selenium
    wordToGuess = (wordList[randint(0,11)])
    #empty variable, will be used for user input later
    wordGuessed = ()
    # word in '-' signs, using the length of the word times the sign -
    blindWord = ('-' * (len(wordToGuess)))
    # same word in list format for easy manipulation
    blindList = [i for i in blindWord]

    #uncomment to see the word (for testing only, don't cheat!!)
    #print(wordToGuess)
    
    while wordGuessed != wordToGuess and (''.join(blindList)) != wordToGuess:
        global errorCount
        #lose condition here.
        if errorCount == 7:
            printHangman()
            print('You dead boy, sorry about that. Better luck next time.')
            playAgain()
        
        #Draw the gallow
        printHangman()
        #Show the word in - signs
        print('The word is: ' + (''.join(blindList)))
        #Ask user for input
        wordGuessed = input('Guess the whole word or type \na letter to see if it is in the word: ').lower()
        #check if user inputs more than 1 lettter if he/she's guessing
        if wordGuessed != wordToGuess and (''.join(blindList)) != wordToGuess and len(wordGuessed) > 1:
            print('Please enter 1 letter at a time, or write the whole word.')
        elif len(wordGuessed) < 1:
            print('Please enter something, you lazy ass!')
        # See if the guessed letter is in the word
        elif wordGuessed in wordToGuess:
            #grab index(es) of letter(s)
            pos = [i for i, char in enumerate(wordToGuess) if char == wordGuessed]
            print('That letter is in the word!')
            #use index(es) provided by pos to change the '-' in blindList
            for p in pos:
                blindList[p] = wordGuessed
        #if the letter is wrong, we add a 1 to the errorCounter, which keeps track of the number
        #of mistakes the player made. We then call the addPart function.
        elif wordGuessed != wordToGuess:
            errorCount += 1
            addPart()
    if wordGuessed == wordToGuess or (''.join(blindList)) == wordToGuess:
        print('Correct! The word was: ' + wordToGuess)
        playAgain()

hangMan()