# Palindrome Number

[![Problem 9](https://img.shields.io/badge/Problem-9-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/palindrome-number/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/palindrome-number/)

**Problem Number:** [9](https://leetcode.com/problems/palindrome-number/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Math
**LeetCode Link:** [https://leetcode.com/problems/palindrome-number/](https://leetcode.com/problems/palindrome-number/)

## Problem Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

**Example 1:**
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

**Example 2:**
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Constraints:**
- `-2^31 <= x <= 2^31 - 1`

## My Approach

I used a **Two Pointer** approach by converting the integer to a string and comparing characters from both ends. The key insight is to use two pointers that move towards each other, comparing characters at each step.

**Algorithm:**
1. Convert the integer to a string
2. Initialize two pointers at the beginning and end of the string
3. Compare characters at both pointers
4. Move pointers towards the center
5. Return true if all comparisons match, false otherwise

## Solution

The solution uses a two-pointer approach on the string representation. See the implementation in the [solution file](../exercises/9.palindrome-number.py).

**Key Points:**
- Converts integer to string for easy character comparison
- Uses two pointers moving from opposite ends
- Handles negative numbers (always false)
- Efficiently compares characters without extra space

## Time & Space Complexity

**Time Complexity:** O(log n)
- Converting to string takes O(log n) time
- Two-pointer comparison takes O(log n) time
- Total: O(log n)

**Space Complexity:** O(log n)
- String conversion requires O(log n) space
- No additional data structures needed

## Key Insights

1. **String Conversion:** Converting to string makes character comparison straightforward.

2. **Two Pointer Technique:** Using pointers from both ends is more efficient than reversing the entire string.

3. **Negative Numbers:** All negative numbers are automatically not palindromes due to the minus sign.

4. **Single Digit:** All single-digit numbers (0-9) are palindromes.

5. **Zero Handling:** Zero is a valid palindrome.

6. **Early Termination:** Can return false as soon as a mismatch is found.

## Mistakes Made

1. **String Conversion Overhead:** Converting to string uses extra space, though it's acceptable for this problem.

2. **Not Using Mathematical Approach:** Could solve without string conversion using mathematical operations.

3. **Edge Case Handling:** Need to ensure proper handling of single digits and zero.

## Related Problems

- **Valid Palindrome** (Problem 125): Check if a string is a palindrome
- **Longest Palindromic Substring** (Problem 5): Find longest palindromic substring
- **Palindrome Linked List** (Problem 234): Check if a linked list is a palindrome
- **Reverse Integer** (Problem 7): Reverse digits of an integer

## Alternative Approaches

1. **Mathematical Approach:** Reverse the number mathematically and compare
2. **Half Reversal:** Only reverse the second half and compare with first half
3. **String Reversal:** Reverse the entire string and compare

## Common Pitfalls

1. **Negative Numbers:** Forgetting that negative numbers are never palindromes.
2. **String Conversion:** Using string conversion when mathematical approach might be preferred.
3. **Zero Handling:** Not properly handling the case where x = 0.
4. **Overflow:** In mathematical approaches, need to handle potential overflow.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/9.palindrome-number.py)](../exercises/9.palindrome-number.py)

*Note: This is a simple problem that introduces the concept of palindrome checking, which is fundamental to many string and number problems.*
