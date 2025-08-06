# Isomorphic Strings

[![Problem 205](https://img.shields.io/badge/Problem-205-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/isomorphic-strings/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/isomorphic-strings/)

**Problem Number:** [205](https://leetcode.com/problems/isomorphic-strings/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Hash Table, String
**LeetCode Link:** [https://leetcode.com/problems/isomorphic-strings/](https://leetcode.com/problems/isomorphic-strings/)

## Problem Description

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**
```
Input: s = "egg", t = "add"
Output: true
```

**Example 2:**
```
Input: s = "foo", t = "bar"
Output: false
```

**Example 3:**
```
Input: s = "paper", t = "title"
Output: true
```

**Constraints:**
- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.

## My Approach

I used a **Hash Table** approach to track character mappings. The key insight is to ensure that each character in s maps to exactly one character in t, and no two characters in s map to the same character in t.

**Algorithm:**
1. Check if strings have same length
2. Use hash table to store character mappings
3. For each character pair:
   - If s[i] not in mapping, check if t[i] is already mapped
   - If t[i] is already mapped, return False
   - Add mapping s[i] -> t[i]
   - If s[i] exists in mapping, verify it maps to t[i]
4. Return True if all mappings are valid

## Solution

The solution uses hash table to track character mappings between strings. See the implementation in the [solution file](../exercises/205.isomorphic-strings.py).

**Key Points:**
- Uses hash table to store character mappings
- Checks for one-to-one mapping requirement
- Verifies existing mappings are consistent
- Handles length mismatch case
- Returns True only if all mappings are valid

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through both strings
- Hash table operations are O(1)
- Total: O(n)

**Space Complexity:** O(k)
- Hash table stores character mappings
- k is the number of unique characters
- In worst case: O(n)

## Key Insights

1. **One-to-One Mapping:** Each character in s must map to exactly one character in t.

2. **No Duplicate Mapping:** No two characters in s can map to the same character in t.

3. **Hash Table:** Using hash table provides O(1) lookup for mappings.

4. **Length Check:** Strings must have same length to be isomorphic.

5. **Bidirectional Check:** Need to check both s->t and t->s mappings.

6. **Character Preservation:** Order of characters must be preserved.

## Mistakes Made

1. **Unidirectional Check:** Initially might only check s->t mapping.

2. **Wrong Logic:** Not checking if t[i] is already mapped to another character.

3. **Complex Implementation:** Overcomplicating the mapping logic.

4. **Missing Edge Cases:** Not handling length mismatch properly.

## Related Problems

- **Word Pattern** (Problem 290): Check if string follows pattern
- **Valid Anagram** (Problem 242): Check if strings are anagrams
- **Group Anagrams** (Problem 49): Group strings by anagrams
- **Longest Substring Without Repeating Characters** (Problem 3): Find unique substring

## Alternative Approaches

1. **Two Hash Tables:** Use separate hash tables for s->t and t->s - O(n) time, O(n) space
2. **Array Mapping:** Use arrays instead of hash tables - O(n) time, O(1) space
3. **Character Frequency:** Use character frequency comparison - O(n) time, O(n) space

## Common Pitfalls

1. **Unidirectional Check:** Only checking s->t mapping.
2. **Wrong Logic:** Not verifying one-to-one mapping requirement.
3. **Complex Implementation:** Overcomplicating the mapping logic.
4. **Missing Edge Cases:** Not handling length mismatch.
5. **Space Inefficiency:** Using unnecessary data structures.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/205.isomorphic-strings.py)](../exercises/205.isomorphic-strings.py)

*Note: This is a string mapping problem that demonstrates efficient character mapping with hash tables.*
