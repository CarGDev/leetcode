# Gray Code

[![Problem 89](https://img.shields.io/badge/Problem-89-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/gray-code/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/gray-code/)

**Problem Number:** [89](https://leetcode.com/problems/gray-code/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Math, Backtracking, Bit Manipulation
**LeetCode Link:** [https://leetcode.com/problems/gray-code/](https://leetcode.com/problems/gray-code/)

## Problem Description

An n-bit gray code sequence is a sequence of `2^n` integers where:

- Every integer is in the inclusive range `[0, 2^n - 1]`
- The first integer is `0`
- An integer appears no more than once in the sequence
- The binary representation of every pair of adjacent integers differs by exactly one bit
- The binary representation of the first and last integers differs by exactly one bit

Given an integer `n`, return any valid n-bit gray code sequence.

**Example 1:**
```
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit
```

**Example 2:**
```
Input: n = 1
Output: [0,1]
```

**Constraints:**
- `1 <= n <= 16`

## My Approach

I used a **Bit Manipulation** approach using the mathematical formula for generating Gray codes. The key insight is that the nth Gray code can be generated using the formula: G(n) = n ⊕ (n >> 1).

**Algorithm:**
1. Generate all numbers from 0 to 2^n - 1
2. For each number, apply the Gray code formula: i ⊕ (i >> 1)
3. Return the list of Gray codes

## Solution

The solution uses bit manipulation with the Gray code formula. See the implementation in the [solution file](../exercises/89.gray-code.py).

**Key Points:**
- Uses the mathematical formula G(n) = n ⊕ (n >> 1)
- Generates all Gray codes in one pass
- Uses bitwise XOR and right shift operations
- Efficient and concise implementation
- Handles all valid values of n

## Time & Space Complexity

**Time Complexity:** O(2^n)
- We generate 2^n Gray codes
- Each Gray code calculation is O(1)
- Total: O(2^n)

**Space Complexity:** O(2^n)
- We store 2^n Gray codes in the result list
- Total: O(2^n)

## Key Insights

1. **Mathematical Formula:** The Gray code can be generated using the formula G(n) = n ⊕ (n >> 1).

2. **Bit Manipulation:** Using bitwise operations (XOR and right shift) is the most efficient approach.

3. **Sequential Generation:** We can generate all Gray codes sequentially without complex logic.

4. **One Bit Difference:** The formula ensures that adjacent numbers differ by exactly one bit.

5. **Circular Property:** The first and last numbers also differ by exactly one bit.

6. **Efficient Implementation:** The list comprehension approach is both readable and efficient.

## Mistakes Made

1. **Complex Backtracking:** Initially might try to use backtracking to generate Gray codes.

2. **Wrong Formula:** Not knowing the mathematical formula for Gray code generation.

3. **Inefficient Approach:** Using recursive or iterative approaches instead of the direct formula.

4. **Bit Manipulation Ignorance:** Not utilizing bitwise operations for efficient computation.

## Related Problems

- **Subsets** (Problem 78): Generate all subsets of a set
- **Subsets II** (Problem 90): Generate subsets with duplicates
- **Permutations** (Problem 46): Generate all permutations
- **Combination Sum** (Problem 39): Find combinations that sum to target

## Alternative Approaches

1. **Backtracking:** Use recursive backtracking to generate Gray codes - O(2^n) time
2. **Iterative Construction:** Build Gray codes iteratively using reflection method
3. **Recursive Construction:** Use recursive approach with mirroring technique

## Common Pitfalls

1. **Complex Implementation:** Using backtracking or complex logic instead of the simple formula.
2. **Wrong Formula:** Not using the correct mathematical formula for Gray code generation.
3. **Bit Manipulation:** Not understanding how to use bitwise operations efficiently.
4. **Performance Issues:** Using inefficient approaches when the formula exists.
5. **Edge Cases:** Not handling n = 1 or other edge cases properly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/89.gray-code.py)](../exercises/89.gray-code.py)

*Note: This is a mathematical problem that demonstrates efficient use of bit manipulation and mathematical formulas.*
