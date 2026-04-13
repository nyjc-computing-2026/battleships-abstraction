# Game data (global)
# This section defines the global data structures used in the game, such
# as the ships and their properties.

BATTLESHIP = {
    "name": "Battleship",
    "symbol": "B",
    "length": 4,
}
CRUISER = {
    "name": "Cruiser",
    "symbol": "C",
    "length": 3,
}
DESTROYER = {
    "name": "Destroyer",
    "symbol": "D",
    "length": 2,
}
SHIP = {
    "B": BATTLESHIP,
    "C": CRUISER,
    "D": DESTROYER,
}

MAX_TURNS = 30


def generate_random_coordinate(n: int) -> tuple[int, int]:
    """Generate a random coordinate (row, column) within the bounds of
    the grid.

    Arguments:
        n: int -- the size of the grid (n x n)

    Returns:
        A tuple containing the row and column indices as integers.
    """
    pass



# Game data: grid
# Grids are represented as nested lists (list of lists), where each
# inner list represents a row of the grid.
# E.g. a 5x5 grid filled with '~' would look like:
# [
#     ['~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~'],
# ]

def create_grid(n: int, placeholder: str) -> list[list[str]]:
    """Create a n-by-n grid.
    The grid is represented as a list of lists.
    Each inner list represents a row.
    Each row is filled with the placeholder character.

    Arguments:
        n: int -- the size of the grid (n x n)
        placeholder: str -- the character to fill the grid with

    Returns:
        A nested list representing the grid.
    """
    pass


def display_grid(grid: list[list[str]]) -> None:
    """Display the grid in a readable format."""
    pass


def initialize_grid(grid: list[list[str]], ships: list[str]) -> None:
    """Initialize the grid by placing ships randomly on the grid."""
    pass


def get_grid_coordinate_char(grid: list[list[str]], x: int, y: int) -> str:
    """Get the character at the specified grid coordinates.

    Arguments:
        grid: list[list[str]] -- the game grid
        x: int -- the row index
        y: int -- the column index
    
    Returns:
        The character at the specified coordinates on the grid.
    """
    pass


# Game data: player
# A player is represented as a dictionary containing their name, ship
# board, attack board, and other relevant information.
# E.g. a player dictionary might look like:
# {
#     'name': 'Player 1',
#     'ship_board': [...],  # A grid representing the player's ships
#     'attack_board': [...],  # A grid representing the player's attacks
#                               on the opponent
#     'ships': {'B': 1, 'C': 1, 'D': 1},  # A dictionary to keep track
#                                           of the player's ships and
#                                           their lengths
#     'turns_taken': 0,  # A counter to track the number of turns taken
#                          by the player
# }

def get_player_input() -> tuple[int, int]:
    """Get the player's input for row and column.
    The function should validate the input to ensure it is within the 
    bounds of the grid.

    Arguments:
        None

    Returns:
        A tuple containing the row and column indices as integers.
    """
    pass


def create_player(name: str) -> dict:
    """Create a player with the given name and an empty grid.

    Arguments:
        name: str -- the name of the player

    Returns:
        A dictionary representing the player, containing their name and grid.
        Format:
        {
            'name': str,
            'ship_board': list[list[str]],
            'attack_board': list[list[str]],
            'ships': dict[str, int],  # A dictionary to keep track of the player's ships and their lengths
            'turns_taken': int,  # A counter to track the number of turns taken by the player
        }
    """
    pass


def update_attack(
        attacker: dict,
        row: int,
        col: int,
        symbol: str
) -> None:
    """Update the attacker's attack board based on the result of an attack.

    Arguments:
        attacker: dict -- the player whose attack board is to be updated
        row: int -- the row index of the attack
        col: int -- the column index of the attack
        symbol: str -- the symbol to represent the attack result on the board

    Returns:
        None
    """
    pass


def update_defense(
        defender: dict,
        row: int,
        col: int,
        symbol: str
) -> None:
    """Update the defender's ship board based on the result of an attack.

    Arguments:
        defender: dict -- the player whose ship board is to be updated
        row: int -- the row index of the attack
        col: int -- the column index of the attack
        symbol: str -- the symbol to represent the attack result on the board

    Returns:
        None
    """
    pass


def has_player_lost(player: dict, max_turns: int) -> bool:
    """Check if the player has lost the game.
    A player loses when:
    - all of their ships have been sunk.
    - they have exceeded the maximum number of turns.

    Arguments:
        player: dict -- the player to check
        max_turns: int -- the maximum number of turns allowed for the player

    Returns:
        True if the player has lost, False otherwise.
    """
    pass


# Main game loop

def main() -> None:
    """Main function to run the Battleship game."""
    computer = create_player("Computer")
    human = create_player("Player")
    max_turns = 30

    # Game setup: populate ship boards and initialize attack boards
    initialize_grid(computer["ship_board"], ["B", "C", "D"])
    initialize_grid(human["ship_board"], ["B", "C", "D"])
    human["turns_taken"] = 0
    computer["turns_taken"] = 0

    # Game loop
    while (
            not has_player_lost(human, max_turns)
            and not has_player_lost(computer, max_turns)
    ):
        # Player's turn
        print(f"{human['name']}'s turn:")
        display_grid(human['attack_board'])
        row, col = get_player_input()
        # Process human's attack on computer's grid
        hit_char = get_grid_coordinate_char(computer['ship_board'], row, col)
        if hit_char in SHIP:
            print(f"Hit! You hit the computer's {SHIP[hit_char]['name']}!")
            # Mark hit on human's attack board
            update_attack(human, row, col, hit_char)
            # Mark hit on computer's ship board
            update_defense(computer, row, col, "X")
        else:
            print("Miss!")
            # Mark miss on human's attack board
            update_attack(human, row, col, "O")
            update_defense(computer, row, col, "O")  # Mark miss on
        human["turns_taken"] += 1

        # Computer's turn
        print(f"{computer['name']}'s turn:")
        display_grid(computer['attack_board'])
        row, col = generate_random_coordinate(len(computer['ship_board']))
        # Process computer's attack on human's grid
        hit_char = get_grid_coordinate_char(human['ship_board'], row, col)
        if hit_char in SHIP:
            print(f"Computer hit your {SHIP[hit_char]['name']}!")
            # Mark hit on computer's attack board
            update_attack(computer, row, col, hit_char)
            # Mark hit on human's ship board
            update_defense(human, row, col, "X")
        else:
            print("Computer missed!")
            # Mark miss on computer's attack board
            update_attack(computer, row, col, "O")
            # Mark miss on human's ship board
            update_defense(human, row, col, "O")
        computer["turns_taken"] += 1


if __name__ == "__main__":
    main()
