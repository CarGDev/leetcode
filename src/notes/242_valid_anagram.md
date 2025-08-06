# Valid Anagram

[![Problem 242](https://img.shields.io/badge/Problem-242-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/valid-anagram/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/valid-anagram/)

**Problem Number:** [242](https://leetcode.com/problems/valid-anagram/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, String, Sorting
**LeetCode Link:** [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

## Problem Description

Given two strings `s` and `t`, return `true` *if* `t` *is an anagram of* `s`*, and* `false` *otherwise*.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**
```
Input: s = "rat", t = "car"
Output: false
```

**Constraints:**
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## My Approach

I used a **Hash Table** approach with Counter to check if two strings are anagrams. The key insight is to compare the character frequency of both strings.

**Algorithm:**
1. Use Counter to count characters in string s
2. Use Counter to count characters in string t
3. Compare the two counters
4. Return True if they are equal, False otherwise

## Solution

The solution uses Counter to efficiently check character frequency. See the implementation in the [solution file](../exercises/242.valid-anagram.py).

**Key Points:**
- Uses Counter for character frequency counting
- Simple one-line comparison
- Handles all edge cases automatically
- Efficient and readable approach

## Time & Space Complexity

**Time Complexity:** O(n)
- Counter creation: O(n) for each string
- Comparison: O(k) where k is number of unique characters
- Total: O(n)

**Space Complexity:** O(k)
- Counter stores frequency of each unique character
- k is the number of unique characters
- In worst case: O(n)

## Key Insights

1. **Character Frequency:** Anagrams have the same character frequency.

2. **Counter Usage:** Using Counter provides efficient character counting.

3. **Simple Comparison:** Direct comparison of counters is sufficient.

4. **Unicode Support:** Counter works with Unicode characters as well.

5. **Case Sensitivity:** The problem specifies lowercase English letters.

6. **Length Check:** Anagrams must have the same length.

## Mistakes Made

1. **Sorting Approach:** Initially might sort strings, leading to O(n log n) complexity.

2. **Manual Counting:** Manually counting characters instead of using Counter.

3. **Complex Logic:** Overcomplicating the anagram check.

4. **Wrong Comparison:** Not using the right data structure for comparison.

## Related Problems

- **Group Anagrams** (Problem 49): Group strings by anagrams
- **Find All Anagrams in a String** (Problem 438): Find anagram substrings
- **Valid Parentheses** (Problem 20): Check valid parentheses
- **Isomorphic Strings** (Problem 205): Check string isomorphism

## Alternative Approaches

1. **Sorting:** Sort both strings and compare - O(n log n) time, O(n) space
2. **Hash Map:** Use manual hash map for counting - O(n) time, O(n) space
3. **Array Counting:** Use array for ASCII characters - O(n) time, O(1) space

## Common Pitfalls

1. **Sorting Usage:** Using sorting when Counter is more efficient.
2. **Manual Counting:** Manually counting characters instead of using Counter.
3. **Complex Logic:** Overcomplicating the anagram check.
4. **Wrong Data Structure:** Not using appropriate data structure for counting.
5. **Case Sensitivity:** Not handling case sensitivity properly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/242.valid-anagram.py)](../exercises/242.valid-anagram.py)

*Note: This is a simple hash table problem that demonstrates efficient anagram checking with Counter.*
