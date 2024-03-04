import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock : 0, peper : 1, scissors : 2
    computer_pick = options[random_number]
    print("Computer picked : ", computer_pick+".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_win += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_win += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_win += 1

    else:
        print("you lost!")
        computer_win += 1
print("You won", user_win, "times.")
print("Computer won", computer_win, "times.")
print("GoodBye!")