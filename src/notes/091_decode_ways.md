# Decode Ways

[![Problem 91](https://img.shields.io/badge/Problem-91-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/decode-ways/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/decode-ways/)

**Problem Number:** [91](https://leetcode.com/problems/decode-ways/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** String, Dynamic Programming
**LeetCode Link:** [https://leetcode.com/problems/decode-ways/](https://leetcode.com/problems/decode-ways/)

## Problem Description

A message containing letters from `A-Z` can be encoded into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `"11106"` can be mapped into:

- `"AAJF"` with the grouping `(1 1 10 6)`
- `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return the number of ways to decode it.

**Example 1:**
```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**
```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

**Example 3:**
```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

**Constraints:**
- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zero(s)

## My Approach

I used a **Dynamic Programming** approach with memoization using recursion. The key insight is to use a recursive function that considers both single-digit and two-digit decoding possibilities at each position.

**Algorithm:**
1. Use a recursive helper function with memoization
2. Base case: if we reach the end of string, return 1 (valid decoding)
3. If current digit is '0', return 0 (invalid)
4. If we're at the last digit, return 1 (single digit decoding)
5. Recursively try single digit decoding (i+1)
6. If two digits form a valid number (1-26), recursively try two digit decoding (i+2)
7. Return sum of both possibilities

## Solution

The solution uses dynamic programming with memoization. See the implementation in the [solution file](../exercises/91.decode-ways.py).

**Key Points:**
- Uses recursive DP with memoization to avoid recalculation
- Handles invalid cases (leading zeros, numbers > 26)
- Considers both single and two-digit decoding at each step
- Uses @lru_cache for automatic memoization
- Returns total number of valid decoding ways

## Time & Space Complexity

**Time Complexity:** O(n)
- Each position is visited once due to memoization
- Each recursive call performs constant time operations
- Total: O(n)

**Space Complexity:** O(n)
- Recursion stack depth: O(n)
- Memoization cache: O(n)
- Total: O(n)

## Key Insights

1. **Recursive DP:** Using recursion with memoization provides a clean solution to this problem.

2. **Two Choices:** At each position, we can either decode one digit or two digits (if valid).

3. **Invalid Cases:** Leading zeros and numbers greater than 26 are invalid and should return 0.

4. **Memoization:** Using @lru_cache prevents recalculating the same subproblems.

5. **Base Cases:** Reaching the end of string means we found a valid decoding.

6. **Optimal Substructure:** The solution for the entire string depends on solutions for substrings.

## Mistakes Made

1. **No Memoization:** Initially might use pure recursion without memoization, leading to exponential complexity.

2. **Wrong Base Cases:** Not properly handling edge cases like leading zeros.

3. **Complex Logic:** Overcomplicating the validation logic for two-digit numbers.

4. **Missing Edge Cases:** Not considering cases where the string is invalid.

## Related Problems

- **Climbing Stairs** (Problem 70): Similar DP pattern with two choices
- **Fibonacci Number** (Problem 509): Classic DP problem
- **Unique Paths** (Problem 62): Grid-based DP problem
- **House Robber** (Problem 198): Another classic DP problem

## Alternative Approaches

1. **Iterative DP:** Use bottom-up dynamic programming - O(n) time, O(n) space
2. **Space Optimized DP:** Use only constant space - O(n) time, O(1) space
3. **Tabulation:** Use iterative approach with table - O(n) time, O(n) space

## Common Pitfalls

1. **Exponential Complexity:** Using recursion without memoization.
2. **Wrong Base Cases:** Not handling leading zeros and invalid numbers.
3. **Complex Validation:** Overcomplicating the two-digit validation logic.
4. **Missing Edge Cases:** Not considering all invalid input cases.
5. **Space Issues:** Not using memoization to avoid redundant calculations.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/91.decode-ways.py)](../exercises/91.decode-ways.py)

*Note: This is a classic dynamic programming problem that demonstrates efficient use of memoization for string decoding.*
