# Week 12: Conway's Game of Life & Knapsack Problem

Complete solutions for Week 12 exercises including all bonus exercises and optional challenge.

## 📁 Files

- **apputil.py** - Main implementation with all exercises
- **test_week12.ipynb** - Comprehensive test notebook
- **exercises.ipynb** - Original exercise notebook (provided)
- **environment.yml** - Conda environment setup

## ✅ Completed Exercises

### Exercise 2: Conway's Game of Life ✓
**Function:** `update_board(current_board)`

Implements one step of Conway's Game of Life following these rules:
1. Any live cell with 2-3 neighbors survives
2. Any dead cell with exactly 3 neighbors becomes alive  
3. All other cells die or stay dead

**Features:**
- Toroidal board (wraps around edges)
- Counts 8 surrounding neighbors for each cell
- Returns updated board as NumPy array

### Bonus Exercise 3: Recursive Game of Life ✓
**Function:** `play_conway_recursive(board=None, steps=10, current_step=0)`

Recursive implementation that:
- Initializes random 10x10 board if not provided
- Recursively updates board for specified steps
- Returns final board state

**Key concepts:**
- Base case: initial random board or max steps reached
- Recursive case: update and recurse with new board
- Tail recursion pattern

### Bonus Exercise 4: Annotated Knapsack Algorithm ✓
**Function:** `knapsack(W, weights, values, full_table=False, names=None)`

Dynamic programming solution with detailed comments explaining:

**Algorithm Explanation:**
The knapsack problem uses a 2D DP table where `table[i][j]` represents the maximum value achievable using the first `i` items with weight capacity `j`. The algorithm builds solutions by considering each item and deciding whether including it yields better value than excluding it.

**Every line is commented** explaining:
- Table initialization (n+1 rows, W+1 columns)
- Base cases (0 items or 0 capacity)
- Decision logic (include vs exclude item)
- Backtracking to find selected items (when names provided)

**Enhanced features:**
- `full_table=True`: Returns complete DP table for analysis
- `names` parameter: Returns selected items, not just max value
- Backtracking algorithm to reconstruct solution

### Optional Challenge: Alternative Solutions ✓
**Functions:**
- `knapsack_solutions(W, weights, values, names=None, top_n=5)`
- `display_knapsack_solutions(W, weights, values, names=None, top_n=5)`

Finds and displays multiple solutions sorted by value:
- Generates all 2^n possible item combinations
- Filters valid solutions (weight ≤ W)
- Sorts by value (descending), then weight (ascending)
- Returns top N alternatives with efficiency metrics

**Features:**
- Shows total value, weight, and items for each solution
- Calculates value/weight efficiency ratio
- Formatted display with rankings
- Useful for exploring trade-offs

## 🎮 Conway's Game of Life Patterns

The implementation correctly handles classic patterns:

### Stable Patterns (Still Lifes)
- **Block** (2x2 square): Remains unchanged
- Never dies, never grows

### Oscillators
- **Blinker** (3-cell line): Alternates horizontal/vertical
- Period 2 (returns to original state after 2 steps)

### Spaceships
- **Glider**: Moves diagonally across board
- Repeats after 4 steps, shifted one cell diagonally

## 📊 Knapsack Problem Examples

### Example 1: Classic Problem
```
Capacity: 50
Weights:  [10, 20, 30]
Values:   [60, 100, 120]

Optimal: Items 2 and 3 (weights 20+30=50, value 100+120=220)
```

### Example 2: With Item Names
```
Capacity: 9 kg
Items:
  Laptop - 2 kg, $3
  Camera - 3 kg, $4
  Book   - 4 kg, $5
  Phone  - 5 kg, $6

Optimal: Camera + Phone (8 kg, $10)
```

## 🚀 How to Run

### Step 1: Setup Environment
```bash
cd D:\week-12
conda env create -f environment.yml
conda activate h501-week-12
```

### Step 2: Test in Jupyter (Recommended)
```bash
# Open Jupyter
jupyter notebook

# Open test_week12.ipynb
# Run all cells to see complete tests
```

### Step 3: Quick Python Test
```python
from apputil import *
import numpy as np

# Test Conway's Game of Life
board = np.array([[0,1,0],
                  [0,1,0],
                  [0,1,0]])
updated = update_board(board)
print(updated)  # Should show vertical to horizontal

# Test Knapsack
weights = [10, 20, 30]
values = [60, 100, 120]
result = knapsack(50, weights, values)
print(f"Max value: {result}")  # Should be 220

# Test Recursive Conway
final = play_conway_recursive(steps=5)
print(f"Live cells after 5 steps: {np.sum(final)}")

# Test Knapsack with names
names = ['Item1', 'Item2', 'Item3']
max_val, items = knapsack(50, weights, values, names=names)
print(f"Selected: {items}")  # Should be ['Item2', 'Item3']
```

### Step 4: Use in exercises.ipynb

Open `exercises.ipynb` and run:

```python
%autoreload 2
from apputil import *
import numpy as np

# Exercise 2: Test update_board
game_board = np.random.randint(2, size=(10, 10))
show_game(game_board, n_steps=5, pause=1)
```

## 🧪 Testing Checklist

- [ ] **Blinker test**: Oscillates between horizontal/vertical ✓
- [ ] **Block test**: Remains stable (unchanged) ✓
- [ ] **Glider test**: Moves diagonally ✓
- [ ] **Random board**: Animates correctly ✓
- [ ] **Recursive function**: Returns valid board ✓
- [ ] **Knapsack basic**: Returns 220 for classic example ✓
- [ ] **Knapsack with names**: Returns correct items ✓
- [ ] **Alternative solutions**: Shows multiple ranked options ✓

## 📚 Key Concepts

### Conway's Game of Life
- **Cellular automaton**: Grid of cells following simple rules
- **Emergent complexity**: Simple rules → complex patterns
- **Toroidal topology**: Board wraps around edges
- **Applications**: Pattern recognition, complexity theory, artificial life

### Dynamic Programming (Knapsack)
- **Optimal substructure**: Optimal solution contains optimal sub-solutions
- **Overlapping subproblems**: Same subproblems solved multiple times
- **Bottom-up approach**: Build table from base cases
- **Time complexity**: O(nW) vs brute force O(2^n)
- **Space complexity**: O(nW) for table

### Recursion
- **Base case**: Condition to stop recursion
- **Recursive case**: Function calls itself with modified input
- **Stack depth**: Each call uses stack space
- **Tail recursion**: Last operation is recursive call (can be optimized)

## 🔍 Algorithm Analysis

### Conway's Game Update
```
Time: O(rows × cols × 9) = O(n) for n cells
Space: O(n) for new board
Each cell checks 8 neighbors (constant time)
```

### Knapsack DP Algorithm
```
Time: O(n × W) where n=items, W=capacity
Space: O(n × W) for DP table
Much faster than brute force O(2^n)

Example: 20 items, W=100
  DP: ~2,000 operations
  Brute force: ~1,000,000 combinations
```

### Recursive Conway
```
Time: O(steps × n) for n cells
Space: O(steps) for recursion stack
Each level computes one update
```

## 🎯 PEP 8 Compliance

All code follows Python style guidelines:
- ✅ Comprehensive docstrings
- ✅ Clear variable naming
- ✅ Proper spacing and indentation
- ✅ Comments explain complex logic
- ✅ Type hints in docstrings
- ✅ Line length < 100 characters

## 💡 Understanding the Algorithms

### Conway's Game Logic
```python
# For each cell, count live neighbors
# Then apply rules:
if cell_alive:
    if neighbors in [2, 3]:
        stay_alive
    else:
        die
else:  # cell dead
    if neighbors == 3:
        become_alive
    else:
        stay_dead
```

### Knapsack Decision Logic
```python
# At each step, choose better option:
include_item = value[i] + table[i-1][remaining_capacity]
exclude_item = table[i-1][current_capacity]

table[i][capacity] = max(include_item, exclude_item)
```

## 🏆 Bonus Features Implemented

1. **Toroidal board** for Conway (edges wrap)
2. **Recursive implementation** with proper base cases
3. **Complete line-by-line comments** for knapsack
4. **Item name tracking** with backtracking
5. **Full DP table** option for analysis
6. **Alternative solutions** ranked by value
7. **Efficiency metrics** (value/weight ratio)
8. **Formatted output** with display function

## 🐛 Common Issues & Solutions

**Issue:** Board doesn't change in Conway
- **Check**: Verify neighbor counting includes all 8 cells
- **Check**: Rules applied correctly (2-3 for alive, exactly 3 for birth)

**Issue:** Knapsack returns wrong value
- **Check**: Using `weights[i-1]` not `weights[i]` (off-by-one)
- **Check**: Comparing `table[i][j]` vs `table[i-1][j]` correctly

**Issue:** Recursive function hits stack limit
- **Solution**: Limit steps to reasonable number (<1000)
- **Python default**: ~1000 recursion depth

## 📖 References

- Conway's Game of Life: https://playgameoflife.com/
- Knapsack Problem: https://en.wikipedia.org/wiki/Knapsack_problem
- Dynamic Programming: Introduction to Algorithms (CLRS), Chapter 15

---

**Author:** Pratik Amrutrao Mane  
**Course:** H501 Applied Data Science  
**Week:** 12 - Time Series & Algorithms  
**Date:** February 2026
