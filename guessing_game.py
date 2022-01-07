import random

def start_game(function_high_score):
    guess_count = 1

    print("Welcome to the Number Guessing Game!")
    if function_high_score != 100000:
        print(f"Current high score is {function_high_score}")
    answer = random.randint(1, 10)
    try:
        player_choice = int(input("Pick a number between 1 - 10:  "))
        while player_choice != answer:
            if player_choice > 10:
                print("Please try again and enter a number inside the range.")
                guess_count += 1
                player_choice = int(input("Pick a number between 1 - 10:  "))
            elif player_choice <= 0:
                print("Please try again and enter a number inside the range.")
                guess_count += 1
                player_choice = int(input("Pick a number between 1 - 10:  "))
            elif player_choice > answer:  
                print("It's lower, guess again.")
                guess_count += 1
                player_choice = int(input("Pick a number between 1 - 10:  "))
            elif player_choice < answer:
                print("It's higher, guess again.")
                guess_count += 1
                player_choice = int(input("Pick a number between 1 - 10:  "))
        if player_choice == answer:
            print(f"You got it right! It took you {guess_count} guesses. This round is over, thanks for playing.")
            if guess_count < function_high_score:
                function_high_score = guess_count
        return function_high_score
    except ValueError:
        print("You need to enter a number that's 1 - 10.  It must be a whole number typed numerically.\n")
        return function_high_score
        

play_again = 'y'
high_score = start_game(100000)

while play_again.lower() != 'n':
    play_again = input("Would you like to play again? [Please choose Y or N]  ")
    if play_again.lower() == 'y':
        high_score = start_game(high_score)
    elif play_again.lower() == 'n':
        print("Thanks for playing, see you next game.")
    else:
        print("Please choose the letter Y or N.")