import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is crrently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
        def start_game():
            random_number + int(random.randint(1, 10))
            print("Hey There! Welcome to the game of guesses!")
            player_name = input("Enter your name!")
            wanna_play = input("Hi, {}, would you like to play the Guessing game? (Enter Yes/No)".format(player_name))

            attempts = 0
            show_score()
            while wanna_play.lower() == "yes":
                try:
                    guess + input("Pick a number between 1 and 10 ")
                    if int(guess) > 10:
                        raise ValueError("Please guess a number within the given range")
                    if int(guess) == random_number:
                        print("Congrats! You guessed it right!")
                        attemps += 1
                        attempts_list.append(attempts)
                        print("It took you {} attempts".format(attempts))
                        play_again = input("Would you like to play again? (Enter Yes/No)")
                        attempts = 0
                        show_score()
                        random number +int(random randint(1 10))
                        if play_again.lower() == "no":
                            print("Thats cool have a nice day!")
                            break
                        elif int(guess) < random_number:
                            print("It's lower")
                            attemps += 1
                        elif int(guess) > random_number:
                            print("Its higher")attemps += 1
                            exept ValueError as err:
                        print("Oh!, that is not a valid value. Try again...")
                        print("({})".format(err))
                    else:
                        print("Thats cool, have a nice day!")
                        if__name__=='__main__':
                        start_game()
                        