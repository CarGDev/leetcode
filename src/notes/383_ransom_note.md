# Ransom Note

[![Problem 383](https://img.shields.io/badge/Problem-383-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/ransom-note/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/ransom-note/)

**Problem Number:** [383](https://leetcode.com/problems/ransom-note/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, String, Counting
**LeetCode Link:** [https://leetcode.com/problems/ransom-note/](https://leetcode.com/problems/ransom-note/)

## Problem Description

Given two strings `ransomNote` and `magazine`, return `true` *if* `ransomNote` *can be constructed by using the letters from* `magazine` *and* `false` *otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**
```
Input: ransomNote = "a", magazine = "b"
Output: false
```

**Example 2:**
```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

**Example 3:**
```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

**Constraints:**
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## My Approach

I used a **Hash Table** approach with Counter to check if ransom note can be constructed. The key insight is to compare character frequencies between ransom note and magazine.

**Algorithm:**
1. Use Counter to count characters in ransom note
2. Use Counter to count characters in magazine
3. Check if ransom note frequency is subset of magazine frequency
4. Return True if all characters can be used, False otherwise

## Solution

The solution uses Counter to efficiently check character frequency requirements. See the implementation in the [solution file](../exercises/383.ransom-note.py).

**Key Points:**
- Uses Counter for frequency counting
- Compares frequency requirements
- Handles all edge cases automatically
- Simple and efficient approach

## Time & Space Complexity

**Time Complexity:** O(n + m)
- Counter creation: O(n) for ransom note, O(m) for magazine
- Frequency comparison: O(k) where k is unique characters
- Total: O(n + m)

**Space Complexity:** O(k)
- Counter stores frequency of each unique character
- k is the number of unique characters
- In worst case: O(n + m)

## Key Insights

1. **Frequency Counting:** Using Counter provides efficient frequency counting.

2. **Subset Check:** Ransom note frequency must be subset of magazine frequency.

3. **Character Reuse:** Each magazine character can only be used once.

4. **Counter Subtraction:** Using Counter subtraction for efficient comparison.

5. **Edge Cases:** Handles empty strings and single characters.

6. **Simple Logic:** The solution logic is straightforward and efficient.

## Mistakes Made

1. **Manual Counting:** Initially might use manual hash table instead of Counter.

2. **Complex Logic:** Overcomplicating the frequency comparison.

3. **Wrong Comparison:** Not understanding the subset relationship.

4. **Inefficient Approach:** Using O(n²) approach when Counter suffices.

## Related Problems

- **Valid Anagram** (Problem 242): Check if strings are anagrams
- **Group Anagrams** (Problem 49): Group strings by anagrams
- **First Unique Character** (Problem 387): Find first unique character
- **Isomorphic Strings** (Problem 205): Check string isomorphism

## Alternative Approaches

1. **Manual Hash Table:** Use manual hash table for counting - O(n + m) time
2. **Array Counting:** Use array for ASCII characters - O(n + m) time, O(1) space
3. **Sorting:** Sort both strings and compare - O(n log n + m log m) time

## Common Pitfalls

1. **Manual Counting:** Using manual hash table instead of Counter.
2. **Complex Logic:** Overcomplicating the frequency comparison.
3. **Wrong Comparison:** Not understanding the subset relationship.
4. **Inefficient Approach:** Using O(n²) approach when Counter suffices.
5. **Character Reuse:** Not considering that each character can only be used once.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/383.ransom-note.py)](../exercises/383.ransom-note.py)

*Note: This is a hash table problem that demonstrates efficient frequency counting and subset checking.*
