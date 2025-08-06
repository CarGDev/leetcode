# Longest Common Prefix

[![Problem 14](https://img.shields.io/badge/Problem-14-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-common-prefix/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-common-prefix/)

**Problem Number:** [14](https://leetcode.com/problems/longest-common-prefix/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** String, Trie
**LeetCode Link:** [https://leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/longest-common-prefix/)

## Problem Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Constraints:**
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters

## My Approach

I used a **Character-by-Character Comparison** approach. The key insight is to compare characters at the same position across all strings, starting from the first character, and stop when we find a mismatch or reach the end of any string.

**Algorithm:**
1. Handle edge cases (empty array, single string)
2. Find the minimum length among all strings
3. Truncate all strings to the minimum length
4. Compare characters at each position across all strings
5. Stop when a mismatch is found
6. Return the common prefix found so far

## Solution

The solution uses character-by-character comparison with optimization. See the implementation in the [solution file](../exercises/14.longest-common-prefix.py).

**Key Points:**
- Finds minimum length to avoid index out of bounds
- Truncates all strings to minimum length for efficiency
- Compares characters at each position across all strings
- Stops at first mismatch and returns prefix up to that point

## Time & Space Complexity

**Time Complexity:** O(S)
- S is the sum of all characters in all strings
- We compare each character at most once
- Finding minimum length: O(n)
- Character comparisons: O(S)

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- No additional data structures proportional to input size

## Key Insights

1. **Character-by-Character Comparison:** The longest common prefix must match at every position across all strings.

2. **Minimum Length Optimization:** By finding the minimum length, we avoid unnecessary comparisons beyond the shortest string.

3. **Early Termination:** We can stop as soon as we find a mismatch at any position.

4. **String Truncation:** Truncating strings to minimum length simplifies the comparison logic.

5. **Edge Cases:** Empty array returns empty string, single string returns itself.

6. **No Common Prefix:** If the first characters don't match, there's no common prefix.

## Mistakes Made

1. **Inefficient Comparison:** Initially might compare entire strings instead of character by character.

2. **Missing Edge Cases:** Not properly handling empty array or single string cases.

3. **Index Out of Bounds:** Not considering that strings might have different lengths.

4. **Unnecessary Complexity:** Overcomplicating the solution with data structures like Trie.

## Related Problems

- **Implement Trie** (Problem 208): Data structure for efficient string operations
- **Word Search** (Problem 79): Finding words in a 2D grid
- **Valid Parentheses** (Problem 20): Pattern matching with symbols
- **Group Anagrams** (Problem 49): Grouping strings by their characteristics

## Alternative Approaches

1. **Horizontal Scanning:** Compare first two strings, then result with next string
2. **Vertical Scanning:** Compare characters at same position across all strings
3. **Divide and Conquer:** Split array in half, find LCP of each half, then combine
4. **Binary Search:** Use binary search on the length of the common prefix

## Common Pitfalls

1. **Index Out of Bounds:** Not handling strings of different lengths properly.
2. **Inefficient Comparison:** Comparing entire strings instead of character by character.
3. **Missing Edge Cases:** Not handling empty array or single string.
4. **Over-engineering:** Using complex data structures when simple comparison suffices.
5. **Wrong Termination:** Not stopping at the first mismatch.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/14.longest-common-prefix.py)](../exercises/14.longest-common-prefix.py)

*Note: This is a fundamental string problem that introduces the concept of finding common patterns across multiple strings.*
