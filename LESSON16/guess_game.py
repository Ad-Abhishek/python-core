import random

player_name = 'PlayerOne'


def hello(name):
    player_name = name
    print(f"Hi {player_name}")

    player_win = 0
    computer_win = 0
    play = True
    while (play):
        num = input("guess the number I'm thinking of...(1 / 2 / 3) \n")
        print(f"{player_name}, you entered {num}")
        number = int(num)

        computer_guess = int(random.choice("123"))
        print(f"I was thinking {computer_guess}")

        if (number == computer_guess):
            print(f"🏆 {player_name}, you win!")
            player_win += 1
        else:
            print(f"😟 sorry, {player_name} you loose!")
            computer_win += 1

        print(f"{player_name}'s win: {player_win}")
        print(f"Total games: {player_win + computer_win}")
        print(
            f"Your winning percentage: {(player_win / (player_win + computer_win))*100} %")

        play_again = input("Play again? (y/n)")
        if (play_again.lower() == 'n'):
            print(f"Bye, {player_name}")
            play = False
        else:
            play = True


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="pass your name as argument"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", help="the name of the player"
    )

    args = parser.parse_args()
    message = hello(args.name)
