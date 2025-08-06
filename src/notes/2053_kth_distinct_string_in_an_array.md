# Kth Distinct String in an Array

[![Problem 2053](https://img.shields.io/badge/Problem-2053-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/kth-distinct-string-in-an-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/kth-distinct-string-in-an-array/)

**Problem Number:** [2053](https://leetcode.com/problems/kth-distinct-string-in-an-array/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Hash Table, String
**LeetCode Link:** [https://leetcode.com/problems/kth-distinct-string-in-an-array/](https://leetcode.com/problems/kth-distinct-string-in-an-array/)

## Problem Description

A **distinct string** is a string that is present only **once** in an array.

Given an array of strings `arr`, and an integer `k`, return *the* `k^th` *distinct string present in* `arr`. If there are **fewer than** `k` distinct strings, return *an **empty string*** `""`.

Note that the strings are considered in the **order in which they appear** in the array.

**Example 1:**
```
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.
```

**Example 2:**
```
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
```

**Example 3:**
```
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
```

**Constraints:**
- `1 <= k <= arr.length <= 1000`
- `1 <= arr[i].length <= 5`
- `arr[i]` consists of lowercase English letters.

## My Approach

I used a **Hash Table** approach to track distinct strings and their order of appearance. The key insight is to maintain two hash tables: one for counting occurrences and another for tracking banned words.

**Algorithm:**
1. Create hash table to track distinct strings
2. Create list to track banned words (non-distinct)
3. For each word in array:
   - If word not in distinct and not banned, add to distinct
   - If word already in distinct, remove from distinct and add to banned
4. Return kth distinct string or empty string if not enough

## Solution

The solution uses hash tables to efficiently track distinct strings in order. See the implementation in the [solution file](../exercises/2053.kth-distinct-string-in-an-array.py).

**Key Points:**
- Uses hash table for O(1) lookup
- Maintains order of appearance
- Tracks banned words to avoid re-adding
- Returns kth distinct string or empty string

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through array: O(n)
- Hash table operations: O(1) average
- Total: O(n)

**Space Complexity:** O(n)
- Hash table for distinct strings: O(n)
- List for banned words: O(n)
- Total: O(n)

## Key Insights

1. **Hash Table:** Using hash table provides efficient string tracking.

2. **Order Preservation:** Maintain order of appearance for distinct strings.

3. **Banned Words:** Track non-distinct words to avoid re-adding them.

4. **Two-Phase Process:** First identify distinct, then find kth.

5. **Edge Cases:** Handle cases with fewer than k distinct strings.

6. **Efficient Removal:** Remove strings from distinct when they become non-distinct.

## Mistakes Made

1. **Wrong Order:** Initially might not preserve order of appearance.

2. **Complex Logic:** Overcomplicating the distinct string tracking.

3. **Re-adding Issue:** Not properly handling banned words.

4. **Inefficient Approach:** Using O(n²) approach when hash table suffices.

## Related Problems

- **First Unique Character** (Problem 387): Find first unique character
- **Contains Duplicate** (Problem 217): Check for duplicates
- **Valid Anagram** (Problem 242): Check if strings are anagrams
- **Group Anagrams** (Problem 49): Group strings by anagrams

## Alternative Approaches

1. **Two Pass:** Count frequencies first, then find kth distinct - O(n) time
2. **Set Operations:** Use set operations for distinct tracking - O(n) time
3. **Sorting:** Sort and find distinct strings - O(n log n) time

## Common Pitfalls

1. **Wrong Order:** Not preserving order of appearance.
2. **Complex Logic:** Overcomplicating the distinct string tracking.
3. **Re-adding Issue:** Not properly handling banned words.
4. **Inefficient Approach:** Using O(n²) approach when hash table suffices.
5. **Edge Cases:** Not handling cases with fewer than k distinct strings.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/2053.kth-distinct-string-in-an-array.py)](../exercises/2053.kth-distinct-string-in-an-array.py)

*Note: This is a hash table problem that demonstrates efficient tracking of distinct elements while preserving order.*
