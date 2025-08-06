# Valid Sudoku

[![Problem 36](https://img.shields.io/badge/Problem-36-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/valid-sudoku/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/valid-sudoku/)

**Problem Number:** [36](https://leetcode.com/problems/valid-sudoku/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Hash Table, Matrix
**LeetCode Link:** [https://leetcode.com/problems/valid-sudoku/](https://leetcode.com/problems/valid-sudoku/)

## Problem Description

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

**Example 1:**
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:**
```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
```

**Constraints:**
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`

## My Approach

I used a **Hash Table** approach to track digits in rows, columns, and 3x3 sub-boxes. The key insight is to use separate hash tables for each row, column, and sub-box to check for duplicates.

**Algorithm:**
1. Initialize hash tables for rows, columns, and sub-boxes
2. Iterate through each cell in the board
3. For each non-empty cell, check if the digit exists in the corresponding row, column, and sub-box
4. If duplicate found, return false
5. Otherwise, add the digit to all three hash tables
6. Return true if no duplicates found

## Solution

The solution uses hash tables to validate Sudoku rules. See the implementation in the [solution file](../exercises/36.valid-sudoku.py).

**Key Points:**
- Uses hash tables to track digits in rows, columns, and sub-boxes
- Maps 3x3 sub-boxes to indices 0-8 based on row and column position
- Checks for duplicates in all three constraints simultaneously
- Handles empty cells ('.') by skipping them
- Returns false immediately when a duplicate is found

## Time & Space Complexity

**Time Complexity:** O(n²)
- We traverse the entire 9x9 board once
- Each cell requires constant time hash table operations
- Total: O(81) = O(n²) where n = 9

**Space Complexity:** O(n²)
- Hash tables for rows: O(n)
- Hash tables for columns: O(n)
- Hash tables for sub-boxes: O(n)
- Total: O(n²)

## Key Insights

1. **Hash Table Efficiency:** Using hash tables provides O(1) lookup time for checking duplicates.

2. **Sub-box Mapping:** The 3x3 sub-boxes can be mapped to indices 0-8 using the formula: `(i//3)*3 + j//3`.

3. **Simultaneous Validation:** We can check all three constraints (row, column, sub-box) for each cell in one pass.

4. **Early Termination:** We can return false immediately when a duplicate is found, avoiding unnecessary checks.

5. **Empty Cell Handling:** Empty cells ('.') should be skipped as they don't affect validity.

6. **Fixed Size:** Since the board is always 9x9, the time and space complexity are effectively constant.

## Mistakes Made

1. **Inefficient Approach:** Initially might use nested loops to check each constraint separately.

2. **Wrong Sub-box Mapping:** Incorrectly calculating the sub-box index for each cell.

3. **Missing Early Termination:** Not returning false immediately when duplicates are found.

4. **Complex Logic:** Overcomplicating the validation with unnecessary conditions.

## Related Problems

- **Sudoku Solver** (Problem 37): Solve a Sudoku puzzle
- **N-Queens** (Problem 51): Place queens on chessboard without conflicts
- **Word Search** (Problem 79): Find words in 2D grid
- **Number of Islands** (Problem 200): Count connected components in grid

## Alternative Approaches

1. **Set-based:** Use sets instead of hash tables for tracking digits
2. **Bit Manipulation:** Use bit masks to represent digits (more memory efficient)
3. **Separate Passes:** Check rows, columns, and sub-boxes in separate passes

## Common Pitfalls

1. **Wrong Sub-box Calculation:** Incorrectly mapping cells to 3x3 sub-boxes.
2. **Inefficient Validation:** Checking constraints separately instead of simultaneously.
3. **Missing Early Termination:** Not stopping when first duplicate is found.
4. **Empty Cell Handling:** Not properly handling '.' characters.
5. **Complex Logic:** Overcomplicating the validation process.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/36.valid-sudoku.py)](../exercises/36.valid-sudoku.py)

*Note: This is a classic matrix validation problem that demonstrates efficient use of hash tables for constraint checking.*
