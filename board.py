import random


class Field:
    def __init__(self):
        """
        Initialize a game field with default attributes.

        Attributes:
            is_covered (bool): Indicates whether the field is covered.
            is_flagged (bool): Indicates whether the field is flagged.
            bomb_placement (bool): Indicates whether a bomb is placed in the field.
            surrounding_bombs (int): Number of surrounding bombs (initially set to 0).
        """
        self.is_covered = True
        self.is_flagged = False
        self.bomb_placement = False
        self.surrounding_bombs = 0

    def toggle_flag(self, action):
        """
        Toggle the flagged status of the field.

        If the field is already flagged and 'flag' action is specified,
        prints a message indicating that the field is already flagged.
        If the field is already uncovered, prints a message indicating that.
        If action = 'flag', flags the field.
        If action = 'unflag', unflags the field if it was previously flagged.

        Args:
            action (str): Specifies whether to flag or unflag the field.

        """
        if action == 'flag':
            if self.is_flagged:
                print("Field already flagged!")
            elif not self.is_covered:
                print("Field already uncovered")
            else:
                self.is_flagged = True
        elif action == 'unflag':
            if self.is_flagged:
                self.is_flagged = False
            else:
                print("Field is not flagged")

    def place_bomb(self):
        """
        Place a bomb in the field if it's not already placed.

        Returns:
            bool: True if a bomb is successfully placed, False if the field already has a bomb.
        """
        if not self.bomb_placement and self.is_covered:
            self.bomb_placement = True
            return True
        else:
            return False

    def uncover(self):
        """
        Toggle the cover status of the field.

        If the field is already uncovered, prints a message indicating that the field is already uncovered.
        Otherwise, uncovers the field.

        """
        if self.is_covered:
            print("Field already uncovered!")
        elif not self.bomb_placement:
            self.is_covered = True

    def set_field_value(self, value):
        """
        Set the number of surrounding bombs for the field.

        Args:
            value (int): The number of surrounding bombs.
        """
        self.surrounding_bombs = value


class Board:
    def __init__(self, size_x, size_y, bombs):
        """
        Initialize a game board with the specified size and number of bombs.

        Args:
            size_x (int): The number of rows in the board.
            size_y (int): The number of columns in the board.
            bombs (int): The number of bombs to be placed on the board.

        """
        self.size_x = size_x
        self.size_y = size_y
        self.num_of_bombs = bombs
        # Create a 2D list to represent the game board with Field objects
        self.board = [[Field() for _ in range(self.size_y)] for _ in range(self.size_x)]

    def starting_setup(self):
        """Initialize the game board by placing bombs and assigning surrounding bomb values."""
        self.place_bombs()
        self.assign_field_values()

    def display(self):
        """
        Display the current state of the game board.

        Prints the game board, revealing flagged cells, uncovered cells with surrounding bomb counts,
        and covered cells with an underscore.

        """
        for i in range(self.size_x):
            for j in range(self.size_y):
                cell = self.board[i][j]

                # Check if the cell is flagged
                if cell.is_flagged:
                    print("F", end=" ")
                # Check if the cell is uncovered
                elif not cell.is_covered:
                    print(cell.surrounding_bombs, end=" ")
                else:
                    # The cell is covered
                    print("_", end=" ")

            # Move to the next line after printing each row
            print("\n")

    def debug_display(self):
        """Display the game board for debugging purposes, showing bombs and surrounding bomb values."""
        print("Debug display:")
        for i in range(self.size_x):
            for j in range(self.size_y):
                if self.board[i][j].is_flagged:
                    print("F", end=" ")
                elif self.board[i][j].bomb_placement:
                    print("B", end=" ")
                else:
                    print(self.board[i][j].surrounding_bombs, end=" ")
            print("\n")

    def place_bombs(self):
        """
        Randomly places bombs on the game board.

        This method randomly selects coordinates on the game board and places bombs
        until the specified number of bombs is reached.

        """
        bomb_placed = 0
        # Loop until the desired number of bombs is placed
        while bomb_placed < self.num_of_bombs:
            # Generate random coordinates
            rand_x, rand_y = random.randint(0, self.size_x - 1), random.randint(0, self.size_y - 1)
            # Check if the bomb was successfully placed
            if self.board[rand_x][rand_y].place_bomb():
                # Increment the count of placed bombs
                bomb_placed += 1

    def assign_field_values(self):
        """
        Assign the 'surrounding_bombs' attribute for each non-bomb cell on the game board.

        Iterates through each cell on the board, calculates the number of surrounding bombs,
        and sets the 'surrounding_bombs' attribute for the current cell.

        The range of neighboring cells is determined by x_beg, x_end, y_beg, and y_end.
        """
        for i in range(self.size_x):
            for j in range(self.size_y):
                if not self.board[i][j].bomb_placement:
                    # Calculate the number of surrounding bombs and set the 'surrounding_bombs' attribute
                    x_beg, x_end = max(0, i - 1), min(self.size_x - 1, i + 1)
                    y_beg, y_end = max(0, j - 1), min(self.size_y - 1, j + 1)

                    count_bombs = sum(self.board[x][y].bomb_placement for x in range(x_beg, x_end + 1)
                                      for y in range(y_beg, y_end + 1))

                    self.board[i][j].set_field_value(count_bombs)

    def reveal_neighbouring(self, x, y):
        """
        Recursively reveals neighboring cells starting from the given coordinates.

        Args:
            x (int): The x-coordinate of the starting cell.
            y (int): The y-coordinate of the starting cell.

        Returns:
            None
        """
        # Base case: If the cell is not covered, return
        if not self.board[x][y].is_covered:
            return

        # Base case: If the cell has surrounding bombs, uncover it and return
        if self.board[x][y].surrounding_bombs != 0:
            self.board[x][y].is_covered = False
            return

        # Recursive case: If the cell has no surrounding bombs, uncover it
        self.board[x][y].is_covered = False

        # Iterate through neighboring cells
        for i in range(-1, 2):
            if 0 <= x + i < self.size_x:
                for j in range(-1, 2):
                    if 0 <= y + j < self.size_y:
                        # Recursively call reveal_neighbouring for neighboring cells
                        self.reveal_neighbouring(x=x + i, y=y + j)
