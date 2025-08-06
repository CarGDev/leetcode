# Generate Parentheses

[![Problem 22](https://img.shields.io/badge/Problem-22-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/generate-parentheses/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/generate-parentheses/)

**Problem Number:** [22](https://leetcode.com/problems/generate-parentheses/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** String, Backtracking, Dynamic Programming
**LeetCode Link:** [https://leetcode.com/problems/generate-parentheses/](https://leetcode.com/problems/generate-parentheses/)

## Problem Description

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**
```
Input: n = 1
Output: ["()"]
```

**Constraints:**
- `1 <= n <= 8`

## My Approach

I used a **Backtracking** approach with recursion. The key insight is to build valid parentheses combinations by tracking the number of opening and closing parentheses used, ensuring we never have more closing than opening parentheses.

**Algorithm:**
1. Handle edge cases (n < 1 returns empty, n == 1 returns ["()"])
2. Use recursion with backtracking to build combinations
3. Track open and close parentheses count
4. Add opening parenthesis if open < n
5. Add closing parenthesis if close < open
6. When open == close == n, add the combination to result
7. Use backtracking to explore all valid combinations

## Solution

The solution uses backtracking with recursion to generate all valid parentheses combinations. See the implementation in the [solution file](../exercises/22.generate-parentheses.py).

**Key Points:**
- Uses backtracking to explore all valid combinations
- Tracks open and close parentheses counts
- Ensures closing parentheses never exceed opening parentheses
- Uses a stack to build combinations and backtrack
- Handles edge cases for n < 1 and n == 1

## Time & Space Complexity

**Time Complexity:** O(4^n/√n)
- This is the Catalan number C(n) = (2n)!/((n+1)!n!)
- Each valid combination requires O(n) time to build
- Total: O(4^n/√n)

**Space Complexity:** O(n)
- Recursion stack depth: O(n)
- Stack for building combinations: O(n)
- Output space: O(4^n/√n) for storing all combinations

## Key Insights

1. **Backtracking Pattern:** This is a classic backtracking problem where we build solutions incrementally and backtrack when constraints are violated.

2. **Parentheses Balance:** The key constraint is that at any point, the number of closing parentheses cannot exceed the number of opening parentheses.

3. **Catalan Numbers:** The number of valid combinations follows the Catalan number sequence.

4. **Recursive Structure:** Each recursive call represents a decision point: add opening parenthesis or closing parenthesis.

5. **Base Case:** When open == close == n, we have a complete valid combination.

6. **Pruning:** We can prune invalid paths early by checking the balance constraint.

## Mistakes Made

1. **Wrong Balance Check:** Initially might not properly check that closing parentheses don't exceed opening parentheses.

2. **Inefficient Generation:** Might generate invalid combinations and then filter them out.

3. **Missing Edge Cases:** Not properly handling n < 1 or n == 1 cases.

4. **Complex Logic:** Overcomplicating the recursion with unnecessary conditions.

## Related Problems

- **Valid Parentheses** (Problem 20): Check if parentheses string is valid
- **Longest Valid Parentheses** (Problem 32): Find longest valid parentheses substring
- **Remove Invalid Parentheses** (Problem 301): Remove minimum parentheses to make valid
- **Check If a Parentheses String Can Be Valid** (Problem 2116): More complex validation

## Alternative Approaches

1. **Dynamic Programming:** Build solutions from smaller subproblems
2. **Iterative:** Use iteration instead of recursion
3. **BFS:** Use breadth-first search to generate combinations level by level

## Common Pitfalls

1. **Wrong Balance Logic:** Not ensuring closing parentheses ≤ opening parentheses.
2. **Inefficient Generation:** Generating invalid combinations and filtering.
3. **Missing Edge Cases:** Not handling n < 1 or n == 1 properly.
4. **Complex Recursion:** Overcomplicating the recursive logic.
5. **Memory Issues:** Not using backtracking efficiently, leading to memory problems.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/22.generate-parentheses.py)](../exercises/22.generate-parentheses.py)

*Note: This is a classic backtracking problem that demonstrates how to generate all valid combinations while respecting constraints.*
