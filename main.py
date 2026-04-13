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

