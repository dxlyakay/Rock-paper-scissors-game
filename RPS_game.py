import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit ").lower()
    if user_input == 'q':
        print('You have exited the game')
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock is 0, papaer is 1, scissors is 2
    computer_pick = options[random_number]
    print('computer picked', computer_pick)

    if user_input == 'rock' and computer_pick == "scissors":
        print('You won!!')
        user_wins += 1


    elif user_input == 'paper' and computer_pick == "rock":
        print('You won!!')
        user_wins += 1


    elif user_input == 'scissors' and computer_pick == "paper":
            print('You won!!')
            user_wins += 1

    else:
        print('you lost')
        computer_wins += 1


    print("you won " + str(user_wins) + " times")
    print("computer won " + str(computer_wins) + " times")
