import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    """
    Execute one step of Conway's Game of Life.
    
    Rules:
    1. Any live cell with 2-3 live neighbors survives
    2. Any dead cell with exactly 3 live neighbors becomes alive
    3. All other cells die or stay dead
    
    Args:
        current_board: Binary NumPy array (1=alive, 0=dead)
        
    Returns:
        Updated board after one step
    """
    rows, cols = current_board.shape
    updated_board = np.zeros_like(current_board)
    
    # Iterate through each cell
    for i in range(rows):
        for j in range(cols):
            # Count live neighbors (8 surrounding cells)
            live_neighbors = 0
            
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    # Skip the cell itself
                    if di == 0 and dj == 0:
                        continue
                    
                    # Calculate neighbor position
                    ni = i + di
                    nj = j + dj
                    
                    # Check if neighbor is within bounds (NO WRAPPING)
                    if 0 <= ni < rows and 0 <= nj < cols:
                        live_neighbors += current_board[ni, nj]
            
            # Apply Conway's Game of Life rules
            if current_board[i, j] == 1:
                # Cell is currently ALIVE
                if live_neighbors == 2 or live_neighbors == 3:
                    updated_board[i, j] = 1  # Survives
                else:
                    updated_board[i, j] = 0  # Dies
            else:
                # Cell is currently DEAD
                if live_neighbors == 3:
                    updated_board[i, j] = 1  # Becomes alive
                else:
                    updated_board[i, j] = 0  # Stays dead
    
    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life.
    """
    for step in range(n_steps):
        clear_output(wait=True)
        game_board = update_board(game_board)
        sns.heatmap(game_board, cmap='tab20c_r', 
                    cbar=False, square=True, linewidths=1)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()
        if step + 1 < n_steps:
            time.sleep(pause)


# Bonus Exercise 3: Recursive Conway's Game of Life
def play_conway_recursive(board=None, steps=10, current_step=0):
    """
    Recursively play Conway's Game of Life.
    """
    if board is None:
        board = np.random.randint(2, size=(10, 10))
        current_step = 0
    
    if current_step >= steps:
        return board
    
    updated_board = update_board(board)
    return play_conway_recursive(updated_board, steps, current_step + 1)


# Bonus Exercise 4: Knapsack Problem
def knapsack(W, weights, values, full_table=False, names=None):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    """
    n = len(values)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weights[i-1] <= j:
                a_1 = values[i-1]
                diff = j - weights[i-1]
                a_2 = table[i-1][diff]
                a = a_1 + a_2
                b = table[i-1][j]
                table[i][j] = max(a, b)
            else:
                table[i][j] = table[i-1][j]
    
    if names is not None:
        selected_items = []
        i = n
        j = W
        while i > 0 and j > 0:
            if table[i][j] != table[i-1][j]:
                selected_items.append(names[i-1])
                j -= weights[i-1]
            i -= 1
        return table[n][W], selected_items[::-1]
    
    if full_table:
        return table
    
    return table[n][W]