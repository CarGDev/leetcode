# Pow(x, n)

[![Problem 50](https://img.shields.io/badge/Problem-50-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/powx-n/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/powx-n/)

**Problem Number:** [50](https://leetcode.com/problems/powx-n/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Math, Recursion
**LeetCode Link:** [https://leetcode.com/problems/powx-n/](https://leetcode.com/problems/powx-n/)

## Problem Description

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

**Example 1:**
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

**Example 2:**
```
Input: x = 2.10000, n = 3
Output: 9.26100
```

**Example 3:**
```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
```

**Constraints:**
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31-1`
- `n` is an integer
- `-10^4 <= x^n <= 10^4`

## My Approach

I used a **Fast Exponentiation** approach with recursion. The key insight is to use the mathematical property that x^n = (x^(n/2))^2 for even n, and x^n = x * (x^(n/2))^2 for odd n, reducing the time complexity from O(n) to O(log n).

**Algorithm:**
1. Handle base case: if n == 0, return 1
2. Handle negative exponent: if n < 0, return 1 / pow(x, |n|)
3. Use recursive fast exponentiation:
   - If n is even: return (x^(n/2))^2
   - If n is odd: return x * (x^(n/2))^2
4. Use helper function to implement the recursive logic

## Solution

The solution uses fast exponentiation with recursion. See the implementation in the [solution file](../exercises/50.powx-n.py).

**Key Points:**
- Uses fast exponentiation to achieve O(log n) time complexity
- Handles negative exponents by taking reciprocal
- Uses recursion with divide-and-conquer approach
- Handles edge cases like n = 0 and negative n
- Efficiently computes large powers

## Time & Space Complexity

**Time Complexity:** O(log n)
- Each recursive call reduces n by half
- Total recursive calls: log₂(n)
- Total: O(log n)

**Space Complexity:** O(log n)
- Recursion stack depth: O(log n)
- Each recursive call uses constant space
- Total: O(log n)

## Key Insights

1. **Fast Exponentiation:** Using the mathematical property x^n = (x^(n/2))^2 reduces complexity from O(n) to O(log n).

2. **Divide and Conquer:** Breaking down the problem into smaller subproblems using recursion.

3. **Negative Exponent Handling:** x^(-n) = 1 / x^n, so we can handle negative exponents by taking the reciprocal.

4. **Even/Odd Split:** Different handling for even and odd exponents optimizes the calculation.

5. **Base Case:** n = 0 always returns 1, providing a clear termination condition.

6. **Overflow Prevention:** The algorithm naturally handles large exponents efficiently.

## Mistakes Made

1. **Linear Approach:** Initially might use a simple loop multiplying x n times, leading to O(n) complexity.

2. **Overflow Issues:** Not considering integer overflow for large exponents.

3. **Negative Exponent:** Forgetting to handle negative exponents properly.

4. **Recursion Depth:** Not considering stack overflow for very large exponents.

## Related Problems

- **Sqrt(x)** (Problem 69): Calculate square root using binary search
- **Super Pow** (Problem 372): Modular exponentiation
- **Factorial Trailing Zeroes** (Problem 172): Count trailing zeros in factorial
- **Count Primes** (Problem 204): Count prime numbers less than n

## Alternative Approaches

1. **Iterative Fast Exponentiation:** Use iteration instead of recursion - O(log n) time, O(1) space
2. **Binary Exponentiation:** Use bit manipulation for even faster computation
3. **Built-in Functions:** Use math.pow() or ** operator (not allowed for this problem)

## Common Pitfalls

1. **Linear Complexity:** Using simple multiplication loop instead of fast exponentiation.
2. **Overflow Handling:** Not considering integer overflow for large exponents.
3. **Negative Exponents:** Incorrectly handling negative exponents.
4. **Recursion Stack:** Not considering stack overflow for very large exponents.
5. **Precision Issues:** Not handling floating-point precision correctly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/50.powx-n.py)](../exercises/50.powx-n.py)

*Note: This is a classic mathematical problem that demonstrates efficient exponentiation using divide-and-conquer recursion.*
