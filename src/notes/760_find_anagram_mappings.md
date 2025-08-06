# Find Anagram Mappings

[![Problem 760](https://img.shields.io/badge/Problem-760-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/find-anagram-mappings/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/find-anagram-mappings/)

**Problem Number:** [760](https://leetcode.com/problems/find-anagram-mappings/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Hash Table
**LeetCode Link:** [https://leetcode.com/problems/find-anagram-mappings/](https://leetcode.com/problems/find-anagram-mappings/)

## Problem Description

Given two lists `A` and `B`, and `B` is an anagram of `A`. `B` is an anagram of `A` means `B` is made by randomizing the order of the elements in `A`.

We want to find an index mapping `P`, from `A` to `B`. A mapping `P[i] = j` means the `i^th` element in `A` appears in `B` at index `j`.

These lists `A` and `B` may contain duplicates. If there are multiple answers, output any of them.

**Example 1:**
```
Input: A = [12, 28, 46, 32, 50], B = [50, 12, 32, 46, 28]
Output: [1, 4, 3, 2, 0]
Explanation:
As P[0] = 1, the 0th element of A appears at B[1], and P[1] = 4, the 1st element of A appears at B[4], and so on.
```

**Example 2:**
```
Input: A = [12, 28, 46, 32, 50], B = [50, 12, 32, 46, 28]
Output: [1, 4, 3, 2, 0]
```

**Constraints:**
- `A, B` have equal lengths in range `[1, 100]`.
- `A[i], B[i]` are integers in range `[0, 10^5]`.

## My Approach

I used a **Hash Table** approach to create a mapping from elements in B to their indices. The key insight is to build a hash table of B's elements and their positions, then use it to find mappings for A.

**Algorithm:**
1. Create hash table to store elements of B and their indices
2. For each element in B, store its index in hash table
3. For each element in A, find its index in B using hash table
4. Return array of indices

## Solution

The solution uses hash table to efficiently find anagram mappings. See the implementation in the [solution file](../exercises/760.find-anagram-mappings.py).

**Key Points:**
- Uses hash table for O(1) lookup
- Maps elements to their indices in B
- Handles duplicates by using first occurrence
- Simple and efficient approach

## Time & Space Complexity

**Time Complexity:** O(n)
- Building hash table: O(n)
- Finding mappings: O(n)
- Total: O(n)

**Space Complexity:** O(n)
- Hash table stores elements and indices
- Total: O(n)

## Key Insights

1. **Hash Table:** Using hash table provides O(1) lookup for element indices.

2. **Anagram Property:** Since B is anagram of A, all elements exist in both arrays.

3. **Duplicate Handling:** Using first occurrence of each element in B.

4. **Index Mapping:** Each element in A maps to its position in B.

5. **Efficient Lookup:** Hash table allows constant time index lookup.

6. **Simple Logic:** The solution logic is straightforward and efficient.

## Mistakes Made

1. **Wrong Mapping:** Initially might map indices incorrectly.

2. **Complex Logic:** Overcomplicating the mapping creation.

3. **Duplicate Issues:** Not handling duplicates properly.

4. **Inefficient Approach:** Using O(n²) approach when hash table suffices.

## Related Problems

- **Valid Anagram** (Problem 242): Check if strings are anagrams
- **Group Anagrams** (Problem 49): Group strings by anagrams
- **Two Sum** (Problem 1): Find pair with target sum
- **Contains Duplicate** (Problem 217): Check for duplicates

## Alternative Approaches

1. **Linear Search:** Use linear search for each element - O(n²) time
2. **Sorting:** Sort both arrays and find mappings - O(n log n) time
3. **Two Hash Tables:** Use separate hash tables for A and B - O(n) time, O(n) space

## Common Pitfalls

1. **Wrong Mapping:** Mapping indices incorrectly.
2. **Complex Logic:** Overcomplicating the mapping creation.
3. **Duplicate Issues:** Not handling duplicates properly.
4. **Inefficient Approach:** Using O(n²) approach when hash table suffices.
5. **Index Confusion:** Confusing indices between A and B.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/760.find-anagram-mappings.py)](../exercises/760.find-anagram-mappings.py)

*Note: This is a hash table problem that demonstrates efficient index mapping for anagram arrays.*
