#A program that plays rock paper cissors with the user
import random
game = input("Do you want to play rock paper scissors? yes/no?\n")
game = game.lower()
usr_math = {"Rock": 3, "Paper": 2, "Scissors": 1}
while game != 'no':
    name = input("What is your name?\n")
    game_start = ['Rock', 'Paper', 'Scissors']
    user_game = random.choice(game_start)
    user_choice = input("Rock, Paper, or Scissors\n")
    user_choice = user_choice.lower()
    user_game = user_game.lower()
    print(user_game)
    print(user_choice)
    if user_choice == user_game:
        print("You Draw!!!")
    elif user_game == "rock" and user_choice == "paper":
        print(f"{name} wins")
    elif user_game == "paper" and user_choice == "scissors":
        print(f"{name} wins")
    elif user_game == "scissors" and user_choice == "paper":
        print(f"CPU Wins, {name} lose")
    else:
        print(f"CPU Wins, {name} lose")
    again = input("Do you want to play again? yes/no?\n")
    again = again.lower()
    if again == "no":
        print("Game Over")
        break
    else:
        continue
    #break