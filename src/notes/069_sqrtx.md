# Sqrt(x)

[![Problem 69](https://img.shields.io/badge/Problem-69-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/sqrtx/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/sqrtx/)

**Problem Number:** [69](https://leetcode.com/problems/sqrtx/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Math, Binary Search
**LeetCode Link:** [https://leetcode.com/problems/sqrtx/](https://leetcode.com/problems/sqrtx/)

## Problem Description

Given a non-negative integer `x`, compute and return the square root of `x`.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

**Note:** You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)`, or `x ** 0.5`.

**Example 1:**
```
Input: x = 4
Output: 2
```

**Example 2:**
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
```

**Constraints:**
- `0 <= x <= 2^31 - 1`

## My Approach

I used a **Binary Search** approach to find the integer square root. The key insight is to search for the largest integer whose square is less than or equal to the given number.

**Algorithm:**
1. Handle edge case: if x == 1, return 1
2. Use binary search with left boundary 1 and right boundary x
3. For each midpoint, calculate its square
4. If square <= x, move left boundary to mid + 1
5. If square > x, move right boundary to mid
6. Return left - 1 (the largest integer whose square <= x)

## Solution

The solution uses binary search to find the integer square root. See the implementation in the [solution file](../exercises/69.sqrtx.py).

**Key Points:**
- Uses binary search to efficiently find square root
- Handles edge case for x = 1
- Searches for largest integer whose square <= x
- Returns integer part only (truncates decimal)
- Avoids using built-in math functions

## Time & Space Complexity

**Time Complexity:** O(log x)
- Binary search halves the search space in each iteration
- Total iterations: log₂(x)
- Total: O(log x)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Binary Search Efficiency:** Binary search provides O(log x) time complexity for finding the square root.

2. **Search Space:** We search from 1 to x, since the square root of x must be in this range.

3. **Integer Truncation:** The problem asks for the integer part only, so we return the largest integer whose square <= x.

4. **Edge Case Handling:** x = 1 is a special case that needs to be handled separately.

5. **Boundary Conditions:** The binary search converges to the correct integer square root.

6. **No Built-in Functions:** The solution avoids using pow() or ** operators as required.

## Mistakes Made

1. **Linear Search:** Initially might use a simple loop to find the square root, leading to O(√x) complexity.

2. **Wrong Boundaries:** Not setting the correct search boundaries for binary search.

3. **Edge Cases:** Not properly handling x = 0 or x = 1.

4. **Return Value:** Not understanding that we need to return left - 1.

## Related Problems

- **Pow(x, n)** (Problem 50): Calculate x raised to power n
- **Search Insert Position** (Problem 35): Find insertion position in sorted array
- **Find First and Last Position of Element in Sorted Array** (Problem 34): Binary search with duplicates
- **Valid Perfect Square** (Problem 367): Check if a number is a perfect square

## Alternative Approaches

1. **Newton's Method:** Use iterative approximation - O(log x) time complexity
2. **Linear Search:** Check each integer from 1 to √x - O(√x) time complexity
3. **Built-in Functions:** Use math.sqrt() or ** 0.5 (not allowed for this problem)

## Common Pitfalls

1. **Wrong Complexity:** Using linear search instead of binary search.
2. **Boundary Errors:** Not setting correct left and right boundaries.
3. **Edge Cases:** Not handling x = 0, x = 1, or very large values.
4. **Return Value:** Not understanding the correct return value from binary search.
5. **Overflow:** Not considering integer overflow for large values.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/69.sqrtx.py)](../exercises/69.sqrtx.py)

*Note: This is a classic binary search problem that demonstrates efficient square root calculation without using built-in functions.*
