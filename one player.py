#A program that plays rock paper cissors with the user
import random
game = input("Do you want to play rock paper scissors? yes/no?\n")
game = game.lower()
usr_math = {"Rock": 3, "Paper": 2, "Scissors": 1}
while game != 'no':
    game_start = ['Rock', 'Paper', 'Scissors']
    user_game = random.choice(game_start)
    user_choice = input("Rock(r), Paper(p), or Scissors(s)\n")
    user_choice = user_choice.lower()
    print(user_game)
    print(user_choice)
    #break