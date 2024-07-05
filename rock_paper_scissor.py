import random

comp_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose One: Rock, Paper, Scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        print("Options not in the list.")
        continue

    random_num = random.randint(0,2)
#   rock = 0, paper = 1, scissor = 2

    computer_pick = options[random_num]
    
    print(f"User picked {user_input.capitalize()}.")
    print(f"Computer picked {computer_pick.capitalize()}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won")
        user_wins+=1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_wins+=1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won")
        user_wins+=1
    
    elif user_input == computer_pick:
        print("Both picked Same, DRAW!")

    else:
        print("You Lost")
        comp_wins+=1

    print(f"Scoreboard - You: {user_wins}, Computer: {comp_wins}")
    
print(f"You Won {user_wins} times."+'\n')
print(f"Computer Won {comp_wins} times."+'\n')
print("GoodBye!")