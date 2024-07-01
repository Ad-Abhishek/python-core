import random
print("Welcome to the game Rock, Paper and Scissors!")

playerchoice = input(
    "Choose your option \n 1. Rock \n 2. Paper \n 3. Scissors \n")

player = int(playerchoice)
print("you chose " + str(player))

computerChoice = random.choice("123")
print("computer chose " + str(computerChoice))

computer = int(computerChoice)

if (player == 1 and computer == 3):
    print("you win!")
elif (player == 2 and computer == 1):
    print("you win!")
elif (player == 3 and computer == 2):
    print("you win!")
elif (player == computer):
    print("its a draw!")
else:
    print("computer wins!")
