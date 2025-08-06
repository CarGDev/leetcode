# Is Subsequence

[![Problem 392](https://img.shields.io/badge/Problem-392-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/is-subsequence/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/is-subsequence/)

**Problem Number:** [392](https://leetcode.com/problems/is-subsequence/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** String, Two Pointers, Dynamic Programming
**LeetCode Link:** [https://leetcode.com/problems/is-subsequence/](https://leetcode.com/problems/is-subsequence/)

## Problem Description

Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`*, or* `false` *otherwise*.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

**Example 1:**
```
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Example 2:**
```
Input: s = "axc", t = "ahbgdc"
Output: false
```

**Constraints:**
- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

**Follow up:** Suppose there are lots of incoming `s`, say `s1, s2, ..., sk` where `k >= 10^9`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

## My Approach

I used a **Two Pointers** approach to check if s is a subsequence of t. The key insight is to use two pointers to traverse both strings and match characters in order.

**Algorithm:**
1. Initialize two pointers i (for t) and j (for s)
2. While j < len(s):
   - If i >= len(t), break (t exhausted)
   - If t[i] == s[j], increment j (match found)
   - Always increment i
3. Return True if j == len(s) (all characters matched)

## Solution

The solution uses two pointers to efficiently check subsequence relationship. See the implementation in the [solution file](../exercises/392.is-subsequence.py).

**Key Points:**
- Uses two pointers for efficient traversal
- Matches characters in order
- Handles edge cases properly
- Simple and efficient approach

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through string t
- Each character is checked at most once
- Total: O(n) where n is length of t

**Space Complexity:** O(1)
- Uses only constant extra space
- No additional data structures needed

## Key Insights

1. **Two Pointers:** Using two pointers allows efficient subsequence checking.

2. **Order Preservation:** Characters must be matched in order.

3. **Greedy Approach:** Always match the first occurrence of each character.

4. **Early Termination:** Can terminate early if t is exhausted.

5. **Edge Cases:** Handles empty strings and single characters.

6. **Follow-up:** Can be optimized for multiple queries using preprocessing.

## Mistakes Made

1. **Wrong Order:** Initially might not preserve character order.

2. **Complex Logic:** Overcomplicating the subsequence check.

3. **Wrong Termination:** Not handling edge cases properly.

4. **Inefficient Approach:** Using O(n²) approach when two pointers suffice.

## Related Problems

- **Longest Common Subsequence** (Problem 1143): Find longest common subsequence
- **Edit Distance** (Problem 72): Calculate edit distance
- **Longest Palindromic Subsequence** (Problem 516): Find longest palindromic subsequence
- **Distinct Subsequences** (Problem 115): Count distinct subsequences

## Alternative Approaches

1. **Dynamic Programming:** Use DP for O(mn) time - O(mn) space
2. **Binary Search:** Use binary search for multiple queries - O(n log n) time
3. **Hash Table:** Use hash table for character positions - O(n) time, O(n) space

## Common Pitfalls

1. **Wrong Order:** Not preserving character order in subsequence.
2. **Complex Logic:** Overcomplicating the subsequence check.
3. **Wrong Termination:** Not handling edge cases properly.
4. **Inefficient Approach:** Using O(n²) approach when two pointers suffice.
5. **Follow-up Challenge:** Not considering optimization for multiple queries.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/392.is-subsequence.py)](../exercises/392.is-subsequence.py)

*Note: This is a two-pointer problem that demonstrates efficient subsequence checking with order preservation.*
