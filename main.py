from play import Play  # Importing the Play class


def main():
    print("Welcome to Minesweeper!")

    # Create an instance of the Play class
    minesweeper_game = Play()

    # Play the Minesweeper game
    minesweeper_game.play()

    print("Thanks for playing Minesweeper!")


if __name__ == "__main__":
    main()
