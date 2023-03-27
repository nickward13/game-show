# set up three doors to choose from

import random


def playGame(switch):
    doors = ["goat", "goat", "goat"]
    doorWithCar = random.randint(1,3)
    doors[doorWithCar-1] = "car"

    # player chooses a door
    # playerChoice = int(input("Choose a door (1, 2, or 3): "))
    playerChoice = random.randint(1,3)
    
    # host opens a door
    hostChoice = random.randint(1,3)
    while hostChoice == playerChoice or doors[hostChoice-1] == "car":
        hostChoice = random.randint(1,3)
    
    if switch == "y":
        if playerChoice == 1:
            if hostChoice == 2:
                playerChoice = 3
            else:
                playerChoice = 2
        elif playerChoice == 2:
            if hostChoice == 1:
                playerChoice = 3
            else:
                playerChoice = 1
        else:
            if hostChoice == 1:
                playerChoice = 2
            else:
                playerChoice = 1

    if(doors[playerChoice-1] == "car"):
        return("win")
    else:
        return("lose")

def play1000Games(switch):
    wins = 0
    losses = 0
    for i in range(0, 1000):
        if(playGame(switch) == "win"):
            wins += 1
        else:
            losses += 1
    if(switch == "n"):
        print("By not switching you won " + str(wins) + " times and lost " + str(losses) + " times.  Win percentage is " + str(wins/(wins+losses)*100) + "%")
    else:
        print("By switching you won " + str(wins) + " times and lost " + str(losses) + " times.  Win percentage is " + str(wins/(wins+losses)*100) + "%")

play1000Games("y")
play1000Games("n")
