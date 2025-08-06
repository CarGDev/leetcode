# Word Pattern

[![Problem 290](https://img.shields.io/badge/Problem-290-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/word-pattern/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/word-pattern/)

**Problem Number:** [290](https://leetcode.com/problems/word-pattern/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, String
**LeetCode Link:** [https://leetcode.com/problems/word-pattern/](https://leetcode.com/problems/word-pattern/)

## Problem Description

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`.

**Example 1:**
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

**Example 2:**
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

**Example 3:**
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

**Constraints:**
- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces `' '`.
- `s` **does not contain** any leading or trailing spaces.
- All the words in `s` are separated by a **single space**.

## My Approach

I used a **Hash Table** approach to check if the string follows the pattern. The key insight is to establish a bijection between pattern characters and words, ensuring one-to-one mapping.

**Algorithm:**
1. Split string s into words
2. Check if pattern length equals number of words
3. First pass: establish mappings for new pattern characters
4. Second pass: verify all mappings are consistent
5. Return True if all checks pass

## Solution

The solution uses hash table to establish and verify bijection between pattern and words. See the implementation in the [solution file](../exercises/290.word-pattern.py).

**Key Points:**
- Uses hash table for character-to-word mapping
- Two-pass approach for verification
- Checks bijection requirement
- Handles length mismatch case

## Time & Space Complexity

**Time Complexity:** O(n)
- Split operation: O(n)
- Two passes through pattern/words: O(n)
- Total: O(n)

**Space Complexity:** O(k)
- Hash table stores character mappings
- k is number of unique characters in pattern
- In worst case: O(n)

## Key Insights

1. **Bijection:** Each pattern character must map to exactly one word, and vice versa.

2. **Two-Pass Approach:** First pass establishes mappings, second pass verifies consistency.

3. **Length Check:** Pattern length must equal number of words.

4. **Hash Table:** Using hash table provides O(1) lookup for mappings.

5. **One-to-One Mapping:** No two characters can map to the same word.

6. **Consistency Check:** All mappings must be consistent throughout the string.

## Mistakes Made

1. **Single Pass:** Initially might try single pass without proper verification.

2. **Wrong Mapping:** Not checking bijection requirement properly.

3. **Complex Logic:** Overcomplicating the mapping verification.

4. **Length Mismatch:** Not handling pattern length vs word count mismatch.

## Related Problems

- **Isomorphic Strings** (Problem 205): Check string isomorphism
- **Valid Anagram** (Problem 242): Check if strings are anagrams
- **Group Anagrams** (Problem 49): Group strings by anagrams
- **Longest Substring Without Repeating Characters** (Problem 3): Find unique substring

## Alternative Approaches

1. **Two Hash Tables:** Use separate hash tables for pattern->word and word->pattern - O(n) time, O(n) space
2. **Single Pass:** Use single pass with immediate verification - O(n) time, O(n) space
3. **Array Mapping:** Use arrays for ASCII characters - O(n) time, O(1) space

## Common Pitfalls

1. **Single Pass:** Using single pass without proper verification.
2. **Wrong Mapping:** Not checking bijection requirement properly.
3. **Complex Logic:** Overcomplicating the mapping verification.
4. **Length Mismatch:** Not handling pattern length vs word count mismatch.
5. **Space Inefficiency:** Using unnecessary data structures.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/290.word-pattern.py)](../exercises/290.word-pattern.py)

*Note: This is a hash table problem that demonstrates efficient bijection checking between pattern and words.*
