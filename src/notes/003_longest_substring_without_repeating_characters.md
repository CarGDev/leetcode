# Longest Substring Without Repeating Characters

[![Problem 3](https://img.shields.io/badge/Problem-3-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**Problem Number:** [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Hash Table, String, Sliding Window
**LeetCode Link:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Constraints:**
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces

## My Approach

I used a **Sliding Window** approach with a hash table to track characters in the current window. The key insight is to maintain a window of unique characters and expand/shrink it as needed.

**Algorithm:**
1. Initialize two pointers (i, j) at the beginning of the string
2. Use a hash table to track characters in the current window
3. Expand the window by moving the right pointer (j) when we encounter a new character
4. Shrink the window by moving the left pointer (i) when we encounter a duplicate
5. Keep track of the maximum window size seen so far
6. Return the maximum length found

## Solution

The solution uses a sliding window approach with hash table optimization. See the implementation in the [solution file](../exercises/3.longest-substring-without-repeating-characters.py).

**Key Points:**
- Uses two pointers to maintain a sliding window
- Hash table tracks characters in the current window
- Expands window when encountering new characters
- Shrinks window when encountering duplicates
- Tracks maximum window size throughout the process

## Time & Space Complexity

**Time Complexity:** O(n)
- We traverse the string once with two pointers
- Hash table operations are O(1) on average
- Each character is visited at most twice (once by each pointer)

**Space Complexity:** O(min(m, n))
- Hash table stores at most min(m, n) characters
- m is the size of the character set (ASCII: 128, Unicode: much larger)
- n is the length of the string

## Key Insights

1. **Sliding Window Pattern:** This is a classic sliding window problem where we maintain a window of unique characters.

2. **Two Pointer Technique:** Using two pointers allows us to efficiently expand and shrink the window without recalculating from scratch.

3. **Hash Table for Tracking:** A hash table provides O(1) lookup to check if a character is already in the current window.

4. **Optimal Window Management:** When we encounter a duplicate, we shrink the window from the left until the duplicate is removed.

5. **Character Frequency vs. Presence:** We only need to track character presence (not frequency) since we want unique characters.

6. **Maximum Tracking:** We need to continuously update the maximum length as we process the string.

## Mistakes Made

1. **Inefficient Window Shrinking:** The current implementation removes characters one by one, which could be optimized.

2. **Character Tracking:** Using a simple dictionary instead of a set might be more appropriate for this use case.

3. **Edge Case Handling:** Need to ensure proper handling of empty strings and single characters.

## Related Problems

- **Longest Substring with At Most Two Distinct Characters** (Problem 159): Similar sliding window with character count limit
- **Longest Substring with At Most K Distinct Characters** (Problem 340): Generalization of the above
- **Minimum Window Substring** (Problem 76): Finding minimum window containing all characters from another string
- **Substring with Concatenation of All Words** (Problem 30): More complex sliding window with word matching

## Alternative Approaches

1. **Brute Force:** Check all possible substrings - O(n³) time complexity
2. **Optimized Brute Force:** Use hash set for each substring - O(n²) time complexity
3. **Character Position Tracking:** Store last position of each character for O(1) window shrinking

## Common Pitfalls

1. **Confusing Substring vs Subsequence:** The problem asks for substring (consecutive characters), not subsequence.
2. **Inefficient Duplicate Removal:** Removing characters one by one can be optimized.
3. **Missing Edge Cases:** Empty string, single character, all same characters.
4. **Character Set Size:** Consider the size of the character set for space complexity.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/3.longest-substring-without-repeating-characters.py)](../exercises/3.longest-substring-without-repeating-characters.py)

*Note: This is a fundamental sliding window problem that introduces the concept of maintaining a dynamic window of unique elements.*
