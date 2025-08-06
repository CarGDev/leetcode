# Factorial Trailing Zeroes

[![Problem 172](https://img.shields.io/badge/Problem-172-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/factorial-trailing-zeroes/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/factorial-trailing-zeroes/)

**Problem Number:** [172](https://leetcode.com/problems/factorial-trailing-zeroes/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Math
**LeetCode Link:** [https://leetcode.com/problems/factorial-trailing-zeroes/](https://leetcode.com/problems/factorial-trailing-zeroes/)

## Problem Description

Given an integer `n`, return the number of trailing zeroes in `n!`.

Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

**Example 1:**
```
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```

**Example 2:**
```
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

**Example 3:**
```
Input: n = 0
Output: 0
```

**Constraints:**
- `0 <= n <= 10^4`

**Follow up:** Could you write a solution that works in logarithmic time complexity?

## My Approach

I used a **Mathematical** approach to count trailing zeroes efficiently. The key insight is that trailing zeroes come from factors of 10, which are created by pairs of 2 and 5. Since there are always more factors of 2 than 5, we only need to count factors of 5.

**Algorithm:**
1. Handle edge case: if n < 5, return 0
2. Initialize counter and power of 5
3. While power of 5 <= n:
   - Add n // power_of_5 to counter
   - Multiply power of 5 by 5
4. Return the total count

## Solution

The solution uses mathematical counting of factors of 5 to find trailing zeroes. See the implementation in the [solution file](../exercises/172.factorial-trailing-zeroes.py).

**Key Points:**
- Counts factors of 5 in factorial
- Uses powers of 5 (5, 25, 125, etc.)
- Handles edge cases properly
- Logarithmic time complexity

## Time & Space Complexity

**Time Complexity:** O(log n)
- Loop runs log₅(n) times
- Each iteration performs constant time operations
- Total: O(log n)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures needed

## Key Insights

1. **Factors of 10:** Trailing zeroes come from factors of 10 (2 × 5).

2. **Factors of 5:** Since there are always more factors of 2 than 5, we only count factors of 5.

3. **Powers of 5:** We need to count factors of 5, 25, 125, etc. (powers of 5).

4. **Mathematical Formula:** The count is ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...

5. **Logarithmic Time:** The loop runs log₅(n) times, giving logarithmic complexity.

6. **Edge Cases:** Numbers less than 5 have no trailing zeroes.

## Mistakes Made

1. **Brute Force:** Initially might calculate the entire factorial, leading to overflow.

2. **Wrong Counting:** Not understanding that we only need to count factors of 5.

3. **Missing Powers:** Not considering higher powers of 5 (25, 125, etc.).

4. **Overflow Issues:** Trying to calculate large factorials directly.

## Related Problems

- **Count Primes** (Problem 204): Count prime numbers less than n
- **Power of Two** (Problem 231): Check if number is power of 2
- **Power of Three** (Problem 326): Check if number is power of 3
- **Add Digits** (Problem 258): Add digits until single digit

## Alternative Approaches

1. **Brute Force:** Calculate factorial and count trailing zeroes - O(n) time, overflow risk
2. **Recursive:** Use recursion to count factors - O(log n) time, O(log n) space
3. **Binary Search:** Use binary search to find factors - O(log² n) time

## Common Pitfalls

1. **Brute Force Calculation:** Trying to calculate large factorials directly.
2. **Wrong Counting:** Not understanding the mathematical relationship with factors of 5.
3. **Missing Powers:** Not considering higher powers of 5 in the counting.
4. **Overflow Issues:** Using integer overflow when calculating factorials.
5. **Complex Logic:** Overcomplicating the mathematical counting.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/172.factorial-trailing-zeroes.py)](../exercises/172.factorial-trailing-zeroes.py)

*Note: This is a mathematical problem that demonstrates efficient counting of trailing zeroes using factors of 5.*
