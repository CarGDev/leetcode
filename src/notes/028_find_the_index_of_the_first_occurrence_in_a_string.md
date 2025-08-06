# Find the Index of the First Occurrence in a String

[![Problem 28](https://img.shields.io/badge/Problem-28-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

**Problem Number:** [28](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** String, Two Pointers, String Matching
**LeetCode Link:** [https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

**Example 2:**
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

**Constraints:**
- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters

## My Approach

I used a **Sliding Window** approach with string slicing. The key insight is to check each possible starting position in the haystack string by comparing substrings of the same length as the needle.

**Algorithm:**
1. Iterate through each possible starting position in haystack
2. Check if the remaining length is sufficient for the needle
3. Compare the substring starting at current position with the needle
4. Return the index if a match is found
5. Return -1 if no match is found

## Solution

The solution uses a sliding window approach with string slicing. See the implementation in the [solution file](../exercises/28.find-the-index-of-the-first-occurrence-in-a-string.py).

**Key Points:**
- Uses sliding window to check each possible starting position
- Compares substrings of needle length with the needle
- Handles edge cases like needle longer than haystack
- Returns first occurrence index or -1 if not found
- Uses string slicing for efficient substring comparison

## Time & Space Complexity

**Time Complexity:** O((n-m+1) × m)
- n is the length of haystack, m is the length of needle
- We check (n-m+1) possible starting positions
- Each substring comparison takes O(m) time
- Total: O((n-m+1) × m) = O(nm) in worst case

**Space Complexity:** O(1)
- Uses only a constant amount of extra space
- String slicing creates temporary strings but doesn't affect asymptotic complexity

## Key Insights

1. **Sliding Window:** Using a sliding window to check each possible starting position for the needle.

2. **String Slicing:** Python's string slicing provides an efficient way to extract substrings for comparison.

3. **Early Termination:** We can stop early if the remaining length is insufficient for the needle.

4. **First Occurrence:** The algorithm naturally finds the first occurrence since we check positions in order.

5. **Edge Case Handling:** Needle longer than haystack automatically returns -1.

6. **Simple Implementation:** This approach is straightforward and easy to understand.

## Mistakes Made

1. **Inefficient Algorithm:** Initially might use a more complex algorithm like KMP when simple sliding window suffices.

2. **Wrong Bounds:** Not properly checking if the remaining length is sufficient for the needle.

3. **Index Confusion:** Returning wrong index or not handling the case where needle is not found.

4. **Over-engineering:** Using complex string matching algorithms when the problem constraints allow simpler solutions.

## Related Problems

- **Repeated String Match** (Problem 686): Find minimum number of times to repeat string
- **Shortest Palindrome** (Problem 214): Find shortest palindrome by adding characters
- **Longest Common Prefix** (Problem 14): Find common prefix among strings
- **Valid Anagram** (Problem 242): Check if two strings are anagrams

## Alternative Approaches

1. **KMP Algorithm:** More efficient for large strings - O(n+m) time complexity
2. **Boyer-Moore Algorithm:** Another efficient string matching algorithm
3. **Rabin-Karp Algorithm:** Uses hashing for string matching
4. **Built-in Methods:** Use str.find() or str.index() (though this might not be the intended solution)

## Common Pitfalls

1. **Wrong Complexity:** Not understanding the time complexity of string slicing.
2. **Bounds Checking:** Not properly checking if there's enough remaining string length.
3. **Index Errors:** Returning wrong index or not handling edge cases.
4. **Over-optimization:** Using complex algorithms when simple approach suffices.
5. **String Comparison:** Not understanding how string comparison works in Python.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/28.find-the-index-of-the-first-occurrence-in-a-string.py)](../exercises/28.find-the-index-of-the-first-occurrence-in-a-string.py)

*Note: This is a fundamental string matching problem that introduces the concept of sliding window for substring search.*
