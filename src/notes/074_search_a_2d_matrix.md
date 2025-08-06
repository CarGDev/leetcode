# Search a 2D Matrix

[![Problem 74](https://img.shields.io/badge/Problem-74-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/search-a-2d-matrix/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/search-a-2d-matrix/)

**Problem Number:** [74](https://leetcode.com/problems/search-a-2d-matrix/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Binary Search, Matrix
**LeetCode Link:** [https://leetcode.com/problems/search-a-2d-matrix/](https://leetcode.com/problems/search-a-2d-matrix/)

## Problem Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example 1:**
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2:**
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

**Constraints:**
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

## My Approach

I used a **Two-Stage Binary Search** approach. The key insight is to first find the correct row using binary search on the first column, then search within that row using another binary search.

**Algorithm:**
1. Use binary search to find the correct row by comparing target with first and last elements of each row
2. If target is within the range of a row, that's our target row
3. Use binary search within the target row to find the element
4. Return true if found, false otherwise

## Solution

The solution uses two-stage binary search for efficient matrix searching. See the implementation in the [solution file](../exercises/74.search-a-2d-matrix.py).

**Key Points:**
- Uses binary search to find the correct row first
- Then uses binary search within the target row
- Handles edge cases where target is at boundaries
- Efficiently narrows down search space in two stages
- Returns boolean indicating if target is found

## Time & Space Complexity

**Time Complexity:** O(log m + log n)
- Row search: O(log m)
- Column search: O(log n)
- Total: O(log m + log n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Two-Stage Search:** The matrix properties allow us to first find the row, then search within that row.

2. **Row Selection:** We can determine which row contains the target by checking if target is within the range of the row's first and last elements.

3. **Binary Search Efficiency:** Using binary search for both stages provides optimal time complexity.

4. **Matrix Properties:** The sorted nature of rows and the relationship between consecutive rows enables efficient search.

5. **Boundary Handling:** We need to check both first and last elements of each row to determine if target is within range.

6. **Early Termination:** We can return false immediately if the target row is not found.

## Mistakes Made

1. **Linear Search:** Initially might use linear search through the entire matrix, leading to O(mn) complexity.

2. **Wrong Row Selection:** Not properly determining which row contains the target.

3. **Complex Logic:** Overcomplicating the search with unnecessary conditions.

4. **Boundary Errors:** Not properly handling edge cases where target is at row boundaries.

## Related Problems

- **Search a 2D Matrix II** (Problem 240): Search in matrix with different properties
- **Binary Search** (Problem 704): Basic binary search implementation
- **Search Insert Position** (Problem 35): Find insertion position in sorted array
- **Find First and Last Position of Element in Sorted Array** (Problem 34): Binary search with duplicates

## Alternative Approaches

1. **Single Binary Search:** Treat matrix as 1D array and use single binary search - O(log(mn)) time
2. **Linear Search:** Search through entire matrix - O(mn) time complexity
3. **Divide and Conquer:** Use recursive approach to divide matrix into quadrants

## Common Pitfalls

1. **Wrong Complexity:** Using linear search instead of binary search.
2. **Incorrect Row Selection:** Not properly determining which row contains the target.
3. **Boundary Issues:** Not handling edge cases where target is at row boundaries.
4. **Complex Implementation:** Overcomplicating the search logic.
5. **Matrix Properties:** Not utilizing the sorted properties of the matrix.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/74.search-a-2d-matrix.py)](../exercises/74.search-a-2d-matrix.py)

*Note: This is a classic binary search problem that demonstrates efficient searching in 2D sorted matrices.*
