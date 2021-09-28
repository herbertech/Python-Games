from random import randint

# list of rock paper scissors
rps = ["rock", "paper", "scissors"]

# computer chooses rock, paper or scissors

computer = rps[randint(0,2)]

# start with false status on player

player = False

while player == False:
    player = input("rock, paper, scissors? Or enter Q to quit. \n").lower()
    if player == "q":
        print("Bye, thanks for playing!")
        exit()
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You Win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You Win!", player, "cuts", computer)
    else:
        print("That is not valid, check spelling and write in lower case letters.")
    player = False
    computer = rps[randint(0,2)]
