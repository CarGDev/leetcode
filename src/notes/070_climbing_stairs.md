# Climbing Stairs

[![Problem 70](https://img.shields.io/badge/Problem-70-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/climbing-stairs/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/climbing-stairs/)

**Problem Number:** [70](https://leetcode.com/problems/climbing-stairs/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Math, Dynamic Programming, Memoization
**LeetCode Link:** [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:**
- `1 <= n <= 45`

## My Approach

I used a **Dynamic Programming** approach with memoization using the Fibonacci sequence. The key insight is that the number of ways to climb n stairs follows the Fibonacci sequence: F(n) = F(n-1) + F(n-2).

**Algorithm:**
1. Use a recursive Fibonacci function with memoization
2. Base cases: F(0) = 0, F(1) = 1
3. For other values: F(n) = F(n-1) + F(n-2)
4. Use cache to store computed values and avoid recalculation
5. Return F(n+1) as the number of ways to climb n stairs

## Solution

The solution uses dynamic programming with memoized Fibonacci sequence. See the implementation in the [solution file](../exercises/70.climbing-stairs.js).

**Key Points:**
- Uses Fibonacci sequence with memoization
- Caches computed values to avoid recalculation
- Handles base cases for n = 0 and n = 1
- Returns F(n+1) for n stairs
- Efficiently computes large values without stack overflow

## Time & Space Complexity

**Time Complexity:** O(n)
- Each Fibonacci number is computed once and cached
- Total computations: O(n)
- Cache lookups: O(1)

**Space Complexity:** O(n)
- Cache array stores up to n Fibonacci numbers
- Recursion stack depth: O(n)
- Total: O(n)

## Key Insights

1. **Fibonacci Sequence:** The number of ways to climb n stairs follows the Fibonacci sequence.

2. **Recurrence Relation:** F(n) = F(n-1) + F(n-2), where F(n) represents ways to climb n stairs.

3. **Memoization:** Caching computed values prevents redundant calculations and improves efficiency.

4. **Base Cases:** F(0) = 0 and F(1) = 1 provide the foundation for the sequence.

5. **Offset:** The answer for n stairs is F(n+1), not F(n).

6. **Optimal Substructure:** The solution for n stairs depends on solutions for n-1 and n-2 stairs.

## Mistakes Made

1. **Naive Recursion:** Initially might use simple recursion without memoization, leading to O(2^n) complexity.

2. **Wrong Base Cases:** Not properly handling the base cases for the Fibonacci sequence.

3. **Missing Offset:** Not understanding that the answer is F(n+1) rather than F(n).

4. **Stack Overflow:** Not considering stack overflow for large values of n.

## Related Problems

- **Fibonacci Number** (Problem 509): Calculate the nth Fibonacci number
- **Min Cost Climbing Stairs** (Problem 746): Climbing stairs with cost
- **Decode Ways** (Problem 91): Decode string to numbers
- **Unique Paths** (Problem 62): Find unique paths in grid

## Alternative Approaches

1. **Iterative DP:** Use bottom-up dynamic programming - O(n) time, O(1) space
2. **Matrix Exponentiation:** Use matrix multiplication - O(log n) time complexity
3. **Binet's Formula:** Use mathematical formula - O(1) time, O(1) space

## Common Pitfalls

1. **Exponential Complexity:** Using naive recursion without memoization.
2. **Wrong Base Cases:** Not properly handling F(0) and F(1).
3. **Missing Offset:** Returning F(n) instead of F(n+1).
4. **Stack Overflow:** Not considering recursion depth for large n.
5. **Memory Issues:** Not using memoization to avoid redundant calculations.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/70.climbing-stairs.js)](../exercises/70.climbing-stairs.js)

*Note: This is a classic dynamic programming problem that demonstrates the relationship between climbing stairs and the Fibonacci sequence.*
