import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

def print_dice(dice_value):
    for line in dice_art[dice_value]:
        print(line)

def initialize_piece(player):
    while True:
        piece_to_initialize = input(f"Player {player}, select a piece to initialize (P1, P2, P3, or P4):\n").upper()
        if piece_to_initialize in players[player]:
            if players[player][piece_to_initialize] == 0:
                players[player][piece_to_initialize] = 1
                break
            else:
                print("Piece already in play. Select a piece not in play.")
        else:
            print("Invalid selection. Choose an available piece.")


players = {1: {"P1": 0, "P2": 0, "P3": 0, "P4": 0}, 2: {"P1": 0, "P2": 0, "P3": 0, "P4": 0}}
first_six = {1: True, 2: True}  # tracking if a player has rolled a six for the first time

# randomizing which player to play first (like a coin toss)
starting_player = 1

current_player = starting_player

print("Welcome to Team 1 Ludo Game Version 2.")

while True:
    roll_input = input(f"Player {current_player}, roll by typing R{current_player}:\n").upper()

    if roll_input == f'R{current_player}':
        dice_value = random.randint(1, 6)

        print(f"Player {current_player} got a {dice_value}")
        print_dice(dice_value)
        print("\n")

        if dice_value == 6 and first_six[current_player]:
            while True:
                piece_to_initialize = input(f"Player {current_player}, select a piece to initialize (P1, P2, P3, or P4):\n").upper()
                if piece_to_initialize in players[current_player]:
                    players[current_player][piece_to_initialize] = 1
                    break
                else:
                    print("Invalid selection. Choose an available piece.")
            
            first_six[current_player] = False
        elif not first_six[current_player]:
            if any(piece > 0 for piece in players[current_player].values()):
                if dice_value == 6 and not first_six[current_player]:
                    while True:
                        update_or_initialize = input(f"Player {current_player}, do you want to update an existing piece (U) or initialize a new one (I)?\n").upper()

                        if update_or_initialize == 'U':
                            piece_to_move = input(f"Player {current_player}, which piece would you like to move (P1, P2, P3, or P4)?\n").upper()

                            if piece_to_move in players[current_player] and players[current_player][piece_to_move] >= 1 and players[current_player][piece_to_move] < 57:
                                break
                            else:
                                print("Invalid move. Choose an available piece that has already started and is on the board.")
                        elif update_or_initialize == 'I':
                            initialize_piece(current_player)
                            break
                        else:
                            print("Invalid input. Type 'U' to update an existing piece or 'I' to initialize a new one.")
                    
                    new_position = players[current_player][piece_to_move] + dice_value

                    if 51 <= players[current_player][piece_to_move] <= 57:
                        remaining_value = 57 - players[current_player][piece_to_move]
                        print(f"Player {current_player} needs a dice value of {remaining_value} to reach position 57 and win.")

                    if new_position <= 57:
                        players[current_player][piece_to_move] = new_position
                    else:
                        print("Invalid move. Piece cannot exceed position 57. Next player's turn.")

                    if new_position > 57 and dice_value == 6:
                        initialize_piece(current_player)
                else:
                    while True:
                        piece_to_move = input(f"Player {current_player}, which piece would you like to move (P1, P2, P3, or P4)?\n").upper()

                        if piece_to_move in players[current_player] and players[current_player][piece_to_move] >= 1 and players[current_player][piece_to_move] < 57:
                            break
                        else:
                            print("Invalid move. Choose an available piece that has already started and is on the board.")
                    
                    new_position = players[current_player][piece_to_move] + dice_value

                    if 51 <= players[current_player][piece_to_move] <= 57:
                        remaining_value = 57 - players[current_player][piece_to_move]
                        print(f"Player {current_player} needs a dice value of {remaining_value} to reach position 57 and win.")

                    if new_position <= 57:
                        players[current_player][piece_to_move] = new_position
                    else:
                        print("Invalid move. Piece cannot exceed position 57. Next player's turn.")

                    if new_position > 57 and dice_value == 6:
                        initialize_piece(current_player)
            else:
                initialize_piece(current_player)
                first_six[current_player] = False

        print("Board Status:")
        for player, pieces in players.items():
            print(f"Player {player}: Positions {pieces}")

        if all(position == 57 for position in players[current_player].values()):
            print(f"Player {current_player} wins the Game!! Game Over.")
            break

        if dice_value != 6:
            current_player = 3 - current_player  # Switch player (1 <-> 2)
    else:
        print(f"Invalid input. Type 'R{current_player}' to roll the dice.")
