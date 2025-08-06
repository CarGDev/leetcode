# Strobogrammatic Number III

[![Problem 248](https://img.shields.io/badge/Problem-248-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/strobogrammatic-number-iii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=HARD)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/strobogrammatic-number-iii/)

**Problem Number:** [248](https://leetcode.com/problems/strobogrammatic-number-iii/)
**Difficulty:** [Hard](https://leetcode.com/problemset/?difficulty=HARD)
**Category:** Math, Recursion, String
**LeetCode Link:** [https://leetcode.com/problems/strobogrammatic-number-iii/](https://leetcode.com/problems/strobogrammatic-number-iii/)

## Problem Description

Given two strings `low` and `high` that represent two integers `low` and `high` where `low <= high`, return *the number of **strobogrammatic numbers** in the range* `[low, high]`.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**
```
Input: low = "50", high = "100"
Output: 3
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
```

**Example 2:**
```
Input: low = "0", high = "0"
Output: 1
```

**Constraints:**
- `1 <= low.length, high.length <= 15`
- `low` and `high` consist of only digits.
- `low <= high`
- `low` and `high` do not contain any leading zeros except itself.

## My Approach

I used a **Recursive Generation** approach to generate all strobogrammatic numbers in the given range. The key insight is to recursively build strobogrammatic numbers of different lengths and count those within the range.

**Algorithm:**
1. Define recursive function to generate strobogrammatic numbers of given length
2. Base cases: length 0 returns [""], length 1 returns ["0","1","8"]
3. For length > 1: recursively generate shorter numbers and add pairs
4. Generate numbers for all lengths between min and max
5. Count numbers that fall within the range [low, high]

## Solution

The solution uses recursive generation to build strobogrammatic numbers and count them in range. See the implementation in the [solution file](../exercises/248.strobogrammatic-number-iii.py).

**Key Points:**
- Uses recursion to generate strobogrammatic numbers
- Handles different lengths systematically
- Avoids leading zeros except for single digit
- Counts numbers within specified range

## Time & Space Complexity

**Time Complexity:** O(5^(n/2))
- Recursive generation: O(5^(n/2)) where n is max length
- Range checking: O(k) where k is number of generated numbers
- Total: O(5^(n/2))

**Space Complexity:** O(5^(n/2))
- Recursive call stack: O(n)
- Generated numbers storage: O(5^(n/2))
- Total: O(5^(n/2))

## Key Insights

1. **Recursive Generation:** Building strobogrammatic numbers recursively is efficient.

2. **Length-based Approach:** Generate numbers by length to avoid duplicates.

3. **Pair Addition:** Add valid pairs (11, 88, 69, 96) around shorter numbers.

4. **Leading Zero Handling:** Avoid leading zeros except for single digit numbers.

5. **Range Checking:** Convert strings to integers for range comparison.

6. **Base Cases:** Handle length 0 and 1 as base cases.

## Mistakes Made

1. **Wrong Generation:** Initially might generate invalid strobogrammatic numbers.

2. **Leading Zeros:** Not properly handling leading zero constraints.

3. **Complex Logic:** Overcomplicating the recursive generation.

4. **Range Issues:** Not properly converting strings to integers for comparison.

## Related Problems

- **Strobogrammatic Number** (Problem 246): Check if number is strobogrammatic
- **Strobogrammatic Number II** (Problem 247): Generate strobogrammatic numbers of given length
- **Generate Parentheses** (Problem 22): Recursive generation
- **Subsets** (Problem 78): Generate all subsets

## Alternative Approaches

1. **Iterative Generation:** Use iteration instead of recursion - O(5^(n/2)) time
2. **Binary Search:** Use binary search on generated numbers - O(n log n) time
3. **Mathematical:** Use mathematical properties to optimize - O(n) time

## Common Pitfalls

1. **Wrong Generation:** Generating invalid strobogrammatic numbers.
2. **Leading Zeros:** Not properly handling leading zero constraints.
3. **Complex Logic:** Overcomplicating the recursive generation.
4. **Range Issues:** Not properly converting strings to integers.
5. **Memory Issues:** Not considering exponential space complexity.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/248.strobogrammatic-number-iii.py)](../exercises/248.strobogrammatic-number-iii.py)

*Note: This is a recursive generation problem that demonstrates efficient strobogrammatic number counting in ranges.*
