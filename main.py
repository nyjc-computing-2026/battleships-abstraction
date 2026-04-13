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
