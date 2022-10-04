#A program that plays rock paper cissors with the user
import random
game = input("Do you want to play rock paper scissors? yes/no?\n")
game = game.lower()
usr_math = {"Rock": 3, "Paper": 2, "Scissors": 1}
while game != 'no':
    name1 = input("What is your name player 1?\n")
    name2 = input("What is your name player 2?\n")
    game_start = ['Rock', 'Paper', 'Scissors']
    user1 = input("Rock, Paper, or Scissors\n")
    user2 = input("Rock, Paper, or Scissors\n")
    user1 = user1.lower()
    user1 = user2.lower()
    print(user1)
    print(user2)
    if user2 == user1:
        print("You Draw!!!")
    elif user1 == "rock" and user2 == "paper":
        print(f"{name2} wins")
    elif user1 == "paper" and user2 == "scissors":
        print(f"{name2} wins")
    elif user1 == "scissors" and user2 == "paper":
        print(f"CPU Wins, {name2} lose")
    else:
        print(f"CPU Wins, {name1} lose")
    again = input("Do you want to play again? yes/no?\n")
    again = again.lower()
    if again == "no":
        print("Game Over")
        break
    else:
        continue
    #break