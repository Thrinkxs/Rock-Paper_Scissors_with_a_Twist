#A program that plays rock paper cissors with the user
import random
game = input("Do you want to play rock paper scissors? yes/no?\n")
game = game.lower()
usr_math = {"Rock": 3, "Paper": 2, "Scissors": 1}
while game != 'no':
    game_start = ['Rock', 'Paper', 'Scissors']
    user_game = random.choice(game)
    user_choice = input("Rock(r), Paper(p), or Scissors(s)\n")
    user_choice = int(user_choice.lower())
    result = abs(user_game - user_choice)
    if not result:
        print('You draw!!!')
    if result == 1:
        if user_game > user_choice:
            print("CPU wins, you lose :( ")
        else:
            print("You win :)")
    else:
        if user_game < user_choice:
            print("You win :)")
        else:
            print("CPU wins, You lose :( ")
