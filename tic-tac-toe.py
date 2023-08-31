import numpy as np


def main():
    # Turns per game
    TURN = 9
    # Define grid for tic-tac-toe
    GRID = np.array([["A0", "A1", "A2"], ["B0", "B1", "B2"], ["C0", "C1", "C2"]])
    # Names players
    PLAYERS = ["Player 1", "Player 2"]

    tic_tac_toe(TURN, GRID, PLAYERS)


# Game
def tic_tac_toe(turn, grid, players):
    grid_game = grid
    turn_game = turn
    # Call print grid
    print_grid(grid_game)

    while turn_game > 0:
        # Turn player 1
        player_1 = get_user(players[0], grid_game)
        update_grid(grid_game, player_1, players[0])

        print_grid(grid_game)
        winner = get_winner(grid_game)
        if winner:
            print(winner)
            break

        # Turn player 2
        player_2 = get_user(players[1], grid_game)
        update_grid(grid_game, player_2, players[1])

        print_grid(grid_game)
        winner = get_winner(grid_game)
        if winner:
            print(winner)
            break


# Function print grid
def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-------------")


# Get choice from players
def get_user(player, grid):
    while True:
        user = input(f"{player} choice: ").strip().upper()
        try:
            row = ord(user[0]) - ord("A")
        except IndexError:
            continue
        try:
            if len(user) > 1 and len(user) < 3:
                col = int(user[1])
            else:
                continue
        except ValueError:
            print("Celda Erronea")
            continue

        if grid[row, col] == "X" or grid[row, col] == "O":
            print("Celda ocupada")
        elif user not in grid:
            print("Celda erronea")
        else:
            return user


# Replace in grid
def update_grid(grid, choice, player):
    row = ord(choice[0]) - ord("A")
    col = int(choice[1])
    if player == "Player 1":
        grid[row, col] = "X"
    elif player == "Player 2":
        grid[row, col] = "O"


def get_winner(grid):
    # Row winner
    for i in range(3):
        if np.count_nonzero(grid[i] == "X") == 3:
            return "Win player 1!"
        elif np.count_nonzero(grid[i] == "O") == 3:
            return "Win player 2!"
    # Column winner
    # Column winner
    for i in range(3):
        if np.count_nonzero(grid[:, i] == "X") == 3:
            return "Win player 1!"
        elif np.count_nonzero(grid[:, i] == "O") == 3:
            return "Win player 2!"

    # Diagonal winner
    win_player1_left = 0
    win_player2_left = 0
    for i in range(3):
        if grid[i][i] == "X":
            win_player1_left += 1
        if grid[i][i] == "O":
            win_player2_left += 1

        if win_player1_left == 3:
            return "Win player 1!"
        if win_player2_left == 3:
            return "Win player 2!"

    win_player1_rigth = 0
    win_player2_rigth = 0
    for i in range(3):
        if grid[i][2 - i] == "X":
            win_player1_rigth += 1
        if grid[i][2 - i] == "O":
            win_player2_rigth += 1

        if win_player1_rigth == 3:
            return "Win player 1!"
        if win_player1_rigth == 3:
            return "Win player 1!"

    return None


if __name__ == "__main__":
    main()
