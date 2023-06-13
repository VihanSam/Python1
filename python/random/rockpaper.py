import random
choices = ["rock","paper","scissors"]
print("Rock Crushs Scissors,Scissors Cuts Paper,Paper Covers Rock")
player = input("Do you want to be Rock Paper Or Scissors(or quit)")

#Score
player_score = 0
computer_score = 0

#Loops
while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("You Choose",choices)
    print("Computer Choose",computer)
    if player == computer:
        print("TIE!")
    elif player == "rock":
        if computer == "scissors":
            player_score = player_score +1
            print("YOU WIN!!!")
            print(player_score,computer_score)
        else:
            print("COMPUTER WINS!!!")
            computer_score = computer_score +1
            print(player_score,computer_score)
    elif player == "paper":
        if computer == "rock":
            player_score = player_score +1
            print("YOU WIN!!!")
            print(player_score,computer_score)
        else:
            print("COMPUTER WINS!!!")
            computer_score = computer_score +1
            print(player_score,computer_score)
    elif player == "scissors":
        if computer == "paper":
            player_score = player_score +1
            print("YOU WIN!!!")
            print(player_score,computer_score)
        else:
            print("COMPUTER WINS!!!")
            computer_score = computer_score +1
            print(player_score,computer_score)
    else:
        print("Invalid Play!")
        
    print()
    player = input("Do you want to be Rock Paper Or Scissors(or quit)")