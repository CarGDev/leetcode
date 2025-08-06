# Group Anagrams

[![Problem 49](https://img.shields.io/badge/Problem-49-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/group-anagrams/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/group-anagrams/)

**Problem Number:** [49](https://leetcode.com/problems/group-anagrams/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Hash Table, String, Sorting
**LeetCode Link:** [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints:**
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters

## My Approach

I used a **Hash Table** approach with sorted string keys. The key insight is to use the sorted version of each string as a key to group anagrams together, since anagrams have the same characters when sorted.

**Algorithm:**
1. Handle edge case: if array has less than 2 elements, return the array as is
2. Create a hash map to store groups of anagrams
3. For each string, sort its characters to create a key
4. Use the sorted string as key and group original strings together
5. Return all groups from the hash map

## Solution

The solution uses a hash table with sorted string keys to group anagrams. See the implementation in the [solution file](../exercises/49.group-anagrams.js).

**Key Points:**
- Uses hash table to group anagrams efficiently
- Sorts characters of each string to create unique keys
- Handles edge cases like empty array or single element
- Groups strings with same sorted representation together
- Returns all groups in any order

## Time & Space Complexity

**Time Complexity:** O(n × k log k)
- n is the number of strings
- k is the maximum length of any string
- Sorting each string takes O(k log k) time
- Total: O(n × k log k)

**Space Complexity:** O(n × k)
- Hash table stores all strings
- Each string can be up to length k
- Total: O(n × k)

## Key Insights

1. **Sorted String as Key:** Anagrams have the same characters when sorted, making them perfect keys for grouping.

2. **Hash Table Efficiency:** Using a hash table provides O(1) average time for insertions and lookups.

3. **Edge Case Handling:** Arrays with less than 2 elements can be returned directly.

4. **Character Sorting:** Sorting characters creates a canonical representation for anagrams.

5. **Grouping Strategy:** All strings with the same sorted representation are anagrams of each other.

6. **Flexible Output:** The problem allows returning groups in any order.

## Mistakes Made

1. **Inefficient Key Generation:** Initially might use character frequency counting instead of sorting.

2. **Wrong Data Structure:** Not using a hash table for efficient grouping.

3. **Edge Case Missing:** Not properly handling arrays with single elements or empty strings.

4. **Complex Logic:** Overcomplicating the grouping process.

## Related Problems

- **Valid Anagram** (Problem 242): Check if two strings are anagrams
- **Find All Anagrams in a String** (Problem 438): Find all anagrams of a pattern in a string
- **Longest Common Prefix** (Problem 14): Find common prefix among strings
- **Group Shifted Strings** (Problem 249): Group strings that can be shifted to each other

## Alternative Approaches

1. **Character Frequency:** Use character count arrays as keys - O(n × k) time
2. **Prime Number Product:** Use product of prime numbers for each character - O(n × k) time
3. **Bit Manipulation:** Use bit masks for character representation (limited to 26 characters)

## Common Pitfalls

1. **Wrong Key Generation:** Not using sorted strings or character frequency as keys.
2. **Inefficient Sorting:** Sorting strings repeatedly instead of using efficient key generation.
3. **Edge Cases:** Not handling arrays with single elements or empty strings.
4. **Memory Usage:** Not considering the space complexity of storing all strings.
5. **Output Format:** Not returning the correct nested array structure.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/49.group-anagrams.js)](../exercises/49.group-anagrams.js)

*Note: This is a classic hash table problem that demonstrates efficient grouping using sorted string keys.*
