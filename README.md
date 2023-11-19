# Minesweeper Game

This is a console-based Minesweeper game implemented in Python. The game allows players to uncover cells on a grid while avoiding hidden bombs.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Features](#features)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/M4rcinGIT/minesweeper.git
    cd minesweeper
    ```

2. Run the game:

    ```bash
    python main.py
    ```

## How to Play

- Launch the game using the instructions in the "Installation" section.
- Choose a difficulty level (easy, intermediate, expert) when prompted.
- Use commands to uncover or flag cells based on the state of the game.

## Features

- Simple console-based interface.
- Three difficulty levels with varying grid sizes and bomb counts.
- Flagging and uncovering cells to avoid bombs.
- Recursive cell uncovering for convenience.

## Code Structure

The project consists of three main classes:

- `Field`: Represents an individual cell on the game board.
- `Board`: Manages the game board, including bomb placement and cell uncovering.
- `Play`: Orchestrates the game, handling player moves and checking game-over conditions.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
