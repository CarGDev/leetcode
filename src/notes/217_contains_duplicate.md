# Contains Duplicate

[![Problem 217](https://img.shields.io/badge/Problem-217-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/contains-duplicate/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/contains-duplicate/)

**Problem Number:** [217](https://leetcode.com/problems/contains-duplicate/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Hash Table, Sorting
**LeetCode Link:** [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

## Problem Description

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## My Approach

I used a **Hash Set** approach to track seen elements. The key insight is to use a set to store elements we've seen and check for duplicates in O(1) time.

**Algorithm:**
1. Initialize an empty set to track seen elements
2. Iterate through each number in the array
3. If number is already in set, return True (duplicate found)
4. Add number to set
5. Return False if no duplicates found

## Solution

The solution uses hash set to efficiently detect duplicates. See the implementation in the [solution file](../exercises/217.contains-duplicate.py).

**Key Points:**
- Uses hash set for O(1) lookup
- Returns True as soon as duplicate is found
- Simple and efficient approach
- Handles all edge cases automatically

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through the array
- Hash set operations are O(1)
- Total: O(n)

**Space Complexity:** O(n)
- Hash set stores at most n elements
- In worst case: O(n)

## Key Insights

1. **Hash Set:** Using hash set provides O(1) lookup time for duplicates.

2. **Early Return:** Return True as soon as first duplicate is found.

3. **Simple Logic:** The solution logic is straightforward and easy to understand.

4. **Efficient Lookup:** Hash set operations are constant time.

5. **Memory Trade-off:** Uses O(n) space for O(n) time complexity.

6. **No Sorting Needed:** Hash set approach doesn't require sorting.

## Mistakes Made

1. **Brute Force:** Initially might use nested loops, leading to O(n²) complexity.

2. **Sorting Approach:** Using sorting when hash set is more efficient.

3. **Complex Logic:** Overcomplicating the duplicate detection.

4. **Wrong Data Structure:** Not using appropriate data structure for O(1) lookup.

## Related Problems

- **Contains Duplicate II** (Problem 219): Check for duplicates within k distance
- **Contains Duplicate III** (Problem 220): Check for duplicates within k distance and t difference
- **Single Number** (Problem 136): Find element appearing once
- **Group Anagrams** (Problem 49): Group strings by anagrams

## Alternative Approaches

1. **Sorting:** Sort array and check adjacent elements - O(n log n) time, O(1) space
2. **Brute Force:** Check all pairs - O(n²) time, O(1) space
3. **Bit Manipulation:** Use bit manipulation for small integers - O(n) time, O(1) space

## Common Pitfalls

1. **Brute Force:** Using nested loops for O(n²) complexity.
2. **Sorting:** Using sorting when hash set is more efficient.
3. **Complex Logic:** Overcomplicating the duplicate detection.
4. **Wrong Data Structure:** Not using hash set for O(1) lookup.
5. **Space Inefficiency:** Using unnecessary data structures.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/217.contains-duplicate.py)](../exercises/217.contains-duplicate.py)

*Note: This is a simple hash table problem that demonstrates efficient duplicate detection.*
