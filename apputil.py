"""
Week 12: Conway's Game of Life and Knapsack Problem

Exercises on cellular automata and dynamic programming.
"""

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
                    
                    # Calculate neighbor position with wrapping (toroidal board)
                    ni = (i + di) % rows
                    nj = (j + dj) % cols
                    
                    live_neighbors += current_board[ni, nj]
            
            # Apply Conway's Game of Life rules
            if current_board[i, j] == 1:
                # Cell is alive
                if live_neighbors in [2, 3]:
                    updated_board[i, j] = 1  # Survives
                else:
                    updated_board[i, j] = 0  # Dies (underpopulation or overpopulation)
            else:
                # Cell is dead
                if live_neighbors == 3:
                    updated_board[i, j] = 1  # Becomes alive (reproduction)
                else:
                    updated_board[i, j] = 0  # Stays dead
    
    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for 
        Conway's Game of Life. In this array, 1 represents a "living" cell 
        and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='tab20c_r', 
                    cbar=False, square=True, linewidths=1)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)


# Bonus Exercise 3: Recursive Conway's Game of Life
def play_conway_recursive(board=None, steps=10, current_step=0):
    """
    Recursively play Conway's Game of Life.
    
    Args:
        board: Current game board (None initializes random 10x10 board)
        steps: Total number of steps to run
        current_step: Current step number (for recursion)
        
    Returns:
        Final board state after all steps
    """
    # Base case: initialize random board on first call
    if board is None:
        board = np.random.randint(2, size=(10, 10))
        current_step = 0
    
    # Base case: reached desired number of steps
    if current_step >= steps:
        return board
    
    # Recursive case: update board and continue
    updated_board = update_board(board)
    
    # Recurse with updated board
    return play_conway_recursive(updated_board, steps, current_step + 1)


# Bonus Exercise 4: Knapsack Problem with Comments
def knapsack(W, weights, values, full_table=False, names=None):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Given items with weights and values, find the combination that maximizes
    total value while staying within weight limit W.
    
    Algorithm Explanation:
    This uses a dynamic programming approach with a 2D table where:
    - Rows represent items (0 to n)
    - Columns represent weight capacities (0 to W)
    - table[i][j] = max value achievable with first i items and capacity j
    
    The algorithm builds up solutions by considering each item and deciding
    whether including it gives better value than excluding it.
    
    Args:
        W: Maximum weight capacity of knapsack
        weights: List of item weights
        values: List of item values
        full_table: If True, return complete DP table
        names: Optional list of item names
        
    Returns:
        Maximum value achievable (or full table if full_table=True)
        If names provided, returns (max_value, selected_items)
    """
    # Get number of items
    n = len(values)
    
    # Create 2D DP table: (n+1) rows x (W+1) columns, initialized to 0
    # Extra row/col for base case (0 items or 0 capacity)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    # Build table in bottom-up manner
    # Iterate through each item (row)
    for i in range(n + 1):
        # Iterate through each weight capacity (column)
        for j in range(W + 1):
            
            # Base case: if no items (i=0) or no capacity (j=0)
            if i == 0 or j == 0:
                # Maximum value is 0
                table[i][j] = 0
            
            # Check if current item can fit in current capacity
            elif weights[i-1] <= j:
                # Option A: Include current item
                # Value of current item
                a_1 = values[i-1]
                # Remaining capacity after including current item
                diff = j - weights[i-1]
                # Best value with remaining capacity from previous items
                a_2 = table[i-1][diff]
                # Total value if we include current item
                a = a_1 + a_2
                
                # Option B: Exclude current item
                # Best value without current item at this capacity
                b = table[i-1][j]
                
                # Choose the option with maximum value
                table[i][j] = max(a, b)
            
            # Current item doesn't fit
            else:
                # Carry forward best value without this item
                table[i][j] = table[i-1][j]
    
    # If names provided, backtrack to find which items were selected
    if names is not None:
        selected_items = []
        i = n
        j = W
        
        # Backtrack through table to find selected items
        while i > 0 and j > 0:
            # If value changed from previous row, item was included
            if table[i][j] != table[i-1][j]:
                selected_items.append(names[i-1])
                # Move to remaining capacity
                j -= weights[i-1]
            # Move to previous item
            i -= 1
        
        # Return max value and selected items (reversed to original order)
        return table[n][W], selected_items[::-1]
    
    # If full table requested, return entire DP table
    if full_table:
        return table
    
    # Return maximum value achievable (bottom-right cell)
    return table[n][W]


# Optional Challenge: Enhanced Knapsack with Alternative Solutions
def knapsack_solutions(W, weights, values, names=None, top_n=5):
    """
    Find multiple knapsack solutions sorted by total value.
    
    Args:
        W: Maximum weight capacity
        weights: List of item weights
        values: List of item values
        names: List of item names
        top_n: Number of alternative solutions to return
        
    Returns:
        List of tuples (total_value, total_weight, selected_items)
        sorted from best to worst
    """
    if names is None:
        names = [f"Item_{i}" for i in range(len(values))]
    
    n = len(values)
    solutions = []
    
    # Generate all possible combinations (2^n)
    for mask in range(1 << n):
        selected_items = []
        total_weight = 0
        total_value = 0
        
        # Check each bit in the mask
        for i in range(n):
            if mask & (1 << i):
                selected_items.append(names[i])
                total_weight += weights[i]
                total_value += values[i]
        
        # Only keep solutions within weight limit
        if total_weight <= W:
            solutions.append((total_value, total_weight, selected_items))
    
    # Sort by value (descending), then by weight (ascending) as tiebreaker
    solutions.sort(key=lambda x: (-x[0], x[1]))
    
    # Return top N solutions
    return solutions[:top_n]


def display_knapsack_solutions(W, weights, values, names=None, top_n=5):
    """
    Display knapsack solutions in a readable format.
    
    Args:
        W: Maximum weight capacity
        weights: List of item weights
        values: List of item values
        names: List of item names
        top_n: Number of solutions to display
    """
    solutions = knapsack_solutions(W, weights, values, names, top_n)
    
    print(f"Knapsack Capacity: {W}")
    print(f"Available items: {len(weights)}")
    print(f"\nTop {len(solutions)} Solutions:\n")
    print("="*70)
    
    for rank, (value, weight, items) in enumerate(solutions, 1):
        print(f"Rank {rank}:")
        print(f"  Total Value:  {value}")
        print(f"  Total Weight: {weight}/{W}")
        print(f"  Items:        {', '.join(items) if items else 'None'}")
        print(f"  Efficiency:   {value/weight:.2f} value/weight" if weight > 0 else "  Efficiency:   N/A")
        print("-"*70)
