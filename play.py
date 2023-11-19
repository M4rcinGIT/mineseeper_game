from board import Board


class Play:
    """
    The Play class represents the core gameplay of Minesweeper.

    Attributes:
        game_on (bool): Indicates whether the game is still in progress.
        board (Board): The game board containing fields and bombs.

    Methods:
        - set_difficulty(): Set the difficulty level for the game.
        - start_game(): Start a new game with the selected difficulty level.
        - get_valid_input(): Get valid user input for checking or flagging a field.
        - make_move(): Process a player's move based on user input.
        - check_if_over(): Check if the game is over by examining the current state of the game board.
        - play(): Start and play the Minesweeper game.
    """

    def __init__(self):
        """
        Initialize a new instance of the Play class.

        Attributes:
            game_on (bool): Indicates whether the game is still in progress.
            board (Board): The game board containing fields and bombs.
        """
        self.game_on = True
        self.board = None

    @staticmethod
    def set_difficulty():
        """
        Set the difficulty level for the game.

        Returns:
            dict: A dictionary containing the size of the board (x, y) and the number of bombs.
        """
        difficulties = {'easy': {"x": 10, "y": 10, "bombs": 10},
                        'intermediate': {"x": 15, "y": 15, "bombs": 40},
                        'expert': {"x": 16, "y": 30, "bombs": 99},
                        'debug': {"x": 5, "y": 5, "bombs": 1}}

        while True:
            difficulty = input("Choose difficulty (EASY/INTERMEDIATE/EXPERT): ").lower()
            if difficulty in difficulties:
                return difficulties[difficulty]
            else:
                print("Invalid input!")

    def start_game(self):
        """
        Start a new game with the selected difficulty level.
        """
        difficulty = self.set_difficulty()
        self.board = Board(difficulty['x'], difficulty['y'], difficulty['bombs'])

    def get_valid_input(self):
        """
        Get valid user input for checking or flagging a field.

        Returns:
            list: A list containing user operation ('c' or 'f' or 'uf')
            and the coordinates (x, y) of the selected field.
        """
        while True:
            user_operation = input("Do you want to check, flag, or unflag the field? C / F / UF: ").lower()
            if user_operation not in ("c", "f", "uf"):
                print("Invalid move! Type C or F or UF")
                continue
            break
        while True:
            try:
                x = int(input("Please enter X coordinate of the field: "))
                y = int(input("Please enter Y coordinate of the field: "))
                if 0 <= x < self.board.size_x and 0 <= y < self.board.size_y:
                    return [user_operation, x, y]
            except ValueError:
                print(f"Invalid! Choose between X: 0-{self.board.size_x - 1}, Y: 0-{self.board.size_y - 1}")

    def make_move(self):
        """
        Process a player's move based on user input.

        Gets a valid move from the player, flags or uncovers the selected cell accordingly,
        and recursively reveals neighboring cells if the selected cell has no surrounding bombs.
        """
        # Get a valid move from the player
        move = self.get_valid_input()

        # Process the move based on the user's input
        if move[0] == 'f':
            # Flag the selected cell
            self.board.board[move[1]][move[2]].toggle_flag('flag')
        if move[0] == 'uf':
            # Unlag the selected cell
            self.board.board[move[1]][move[2]].toggle_flag('unflag')
        elif move[0] == 'c':
            # Uncover the selected cell
            self.board.board[move[1]][move[2]].uncover()

            # If the cell has no surrounding bombs, reveal neighboring cells
            if self.board.board[move[1]][move[2]].surrounding_bombs == 0:
                self.board.reveal_neighbouring(move[1], move[2])

    def check_if_over(self):
        """
        Check if the game is over by examining the current state of the game board.

        If the player has uncovered a cell with a bomb, the game ends in defeat.
        If all bombs are correctly flagged, the game ends in victory.

        Prints a corresponding message and updates the game status accordingly.
        """
        flag_counter = 0

        # Iterate through each cell on the game board
        for i in range(self.board.size_x):
            for j in range(self.board.size_y):
                # Check if the cell has a bomb and is uncovered
                if (not self.board.board[i][j].is_covered
                        and self.board.board[i][j].bomb_placement):
                    print("Game over, you've hit the bomb!!!")
                    self.game_on = False

                # Check if the cell is flagged and has a bomb
                if self.board.board[i][j].is_flagged and self.board.board[i][j].bomb_placement:
                    flag_counter += 1

        # Check if all bombs are correctly flagged
        if flag_counter == self.board.num_of_bombs:
            print("Game over, you won! All bombs are flagged!")
            self.game_on = False

    def play(self):
        """
        Start and play the Minesweeper game.

        Initiates the game, sets up the initial game state, displays the initial board,
        and continues to prompt the player for moves until the game is over.
        """
        # Start a new game
        self.start_game()

        # Set up the initial game state
        self.board.starting_setup()

        # Display the initial board (for debugging purposes)
        self.board.debug_display()

        # Continue playing until the game is over
        while self.game_on:
            # Process the player's move
            self.make_move()

            # Display the updated game board
            self.board.display()

            # Check if the game is over
            self.check_if_over()
