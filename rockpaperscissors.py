from random import randint
import time
#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False
rounds = int(input("how many games would you like to play?  "))
time.sleep(1)
no_rounds= (range(rounds))
for round in no_rounds:
    time.sleep(1)
    print("Round {}".format(round))

    while player == False:
    #set player to True
        player = input("Rock, Paper, Scissors?  ")
        if player == computer:
            print("Tie!")
        elif player.lower() == "rock":
            if computer.lower() == "paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player.lower() == "paper":
            if computer.lower() == "scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player.lower() == "scissors":
            if computer.lower() == "rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]