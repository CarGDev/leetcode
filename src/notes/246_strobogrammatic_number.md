# Strobogrammatic Number

[![Problem 246](https://img.shields.io/badge/Problem-246-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/strobogrammatic-number/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/strobogrammatic-number/)

**Problem Number:** [246](https://leetcode.com/problems/strobogrammatic-number/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, String, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/strobogrammatic-number/](https://leetcode.com/problems/strobogrammatic-number/)

## Problem Description

Given a string `num` which represents an integer, return `true` *if* `num` *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**
```
Input: num = "69"
Output: true
```

**Example 2:**
```
Input: num = "88"
Output: true
```

**Example 3:**
```
Input: num = "962"
Output: false
```

**Constraints:**
- `1 <= num.length <= 50`
- `num` consists of only digits.

## My Approach

I used a **Two Pointers** approach with hash map mapping to check if a number is strobogrammatic. The key insight is to use a mapping of valid strobogrammatic digits and check from both ends.

**Algorithm:**
1. Define mapping of valid strobogrammatic digits
2. Use two pointers (left, right) starting from both ends
3. While left <= right:
   - Check if both digits are in mapping
   - Check if left digit maps to right digit
   - Move pointers inward
4. Return True if all checks pass

## Solution

The solution uses two pointers with hash map mapping to check strobogrammatic numbers. See the implementation in the [solution file](../exercises/246.strobogrammatic-number.py).

**Key Points:**
- Uses hash map for digit mapping
- Two-pointer approach from both ends
- Checks validity of each digit pair
- Handles odd and even length numbers

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through the string
- Each iteration performs constant time operations
- Total: O(n)

**Space Complexity:** O(1)
- Hash map has constant size (5 mappings)
- Total: O(1)

## Key Insights

1. **Digit Mapping:** Only certain digits (0,1,6,8,9) are valid strobogrammatic.

2. **Two Pointers:** Using two pointers from both ends is efficient.

3. **Pair Checking:** Each pair of digits must map correctly.

4. **Center Digit:** For odd length, center digit must map to itself.

5. **Valid Digits:** Only 0,1,6,8,9 are valid strobogrammatic digits.

6. **Mapping Rules:** 6↔9, 0↔0, 1↔1, 8↔8.

## Mistakes Made

1. **Wrong Mapping:** Initially might use incorrect digit mappings.

2. **Complex Logic:** Overcomplicating the strobogrammatic check.

3. **Wrong Order:** Not checking digits in correct order.

4. **Missing Digits:** Not including all valid strobogrammatic digits.

## Related Problems

- **Strobogrammatic Number II** (Problem 247): Generate strobogrammatic numbers
- **Strobogrammatic Number III** (Problem 248): Count strobogrammatic numbers in range
- **Valid Palindrome** (Problem 125): Check if string is palindrome
- **Palindrome Number** (Problem 9): Check if number is palindrome

## Alternative Approaches

1. **String Reversal:** Reverse string and apply mapping - O(n) time, O(n) space
2. **Single Pass:** Use single pointer with length calculation - O(n) time, O(1) space
3. **Recursive:** Use recursion to check pairs - O(n) time, O(n) space

## Common Pitfalls

1. **Wrong Mapping:** Using incorrect digit mappings.
2. **Complex Logic:** Overcomplicating the strobogrammatic check.
3. **Wrong Order:** Not checking digits in correct order.
4. **Missing Digits:** Not including all valid strobogrammatic digits.
5. **Center Handling:** Not properly handling center digit for odd length.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/246.strobogrammatic-number.py)](../exercises/246.strobogrammatic-number.py)

*Note: This is a two-pointer problem that demonstrates efficient strobogrammatic number checking with digit mapping.*
