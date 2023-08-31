import numpy as np

def main():
    # Turns per game
    TURN = 9
    # Define grid for tic-tac-toe
    GRID =  np.array([["A0", "A1", "A2"], ["B0", "B1", "B2"], ["C0", "C1", "C2"]])
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
        player_1 = get_user(players[0],grid_game)
        update_grid(grid_game, player_1, players[0])


        print_grid(grid_game)

        # Turn player 2
        player_2 = get_user(players[1],grid_game)
        update_grid(grid_game, player_2, players[1])
        

        

        print_grid(grid_game)
    

        


# def turn_player_one():

# def turn_player_one():


# Function print grid
def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-------------")

# Get choice from players
def get_user(player, grid):
    while True:
        user = input(f"{player} choice: ").strip().upper()
        row = ord(user[0]) - ord('A')
        try:
            col = int(user[1])
        except ValueError:
            print('Celda Erronea')
            continue
        
        if grid[row, col] == 'X' or grid[row, col] == 'O':
            print('Celda ocupada')
        elif user not in grid:
            print('Celda erronea')
        else:
            return user

# Replace in grid
def update_grid(grid, choice, player):
    row = ord(choice[0]) - ord('A')
    col = int(choice[1])
    if player == "Player 1":
        grid[row, col] = 'X'
    elif player == "Player 2":
        grid[row, col] = 'O'

def get_winner(grid_game):
    # Row winner
    for i in range(3):
        if grid_game[i].count('X') == 3:
            return True
        elif grid_game[i].count('O') == 3:
            return True
    # Column winner
        #i = 0
#while i < 3:
 #   if x[i][i] == 'X':
   #     print(x[i][i])
  #      i += 1
    

    # Diagonal winner



if __name__ == "__main__":
    main()
