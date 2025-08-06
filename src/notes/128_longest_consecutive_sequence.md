# Longest Consecutive Sequence

[![Problem 128](https://img.shields.io/badge/Problem-128-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-consecutive-sequence/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/longest-consecutive-sequence/)

**Problem Number:** [128](https://leetcode.com/problems/longest-consecutive-sequence/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Hash Table, Union Find
**LeetCode Link:** [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

**Example 1:**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2:**
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Constraints:**
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## My Approach

I used a **Hash Set** approach with sorting to find the longest consecutive sequence. The key insight is to remove duplicates, sort the array, and then count consecutive sequences.

**Algorithm:**
1. Handle edge cases (empty array or single element)
2. Convert array to set to remove duplicates
3. Sort the unique elements
4. Iterate through sorted elements to find consecutive sequences
5. Track the length of current consecutive sequence
6. Update maximum length when sequence breaks
7. Return the maximum consecutive sequence length

## Solution

The solution uses hash set and sorting to find the longest consecutive sequence. See the implementation in the [solution file](../exercises/128.longest-consecutive-sequence.py).

**Key Points:**
- Removes duplicates using set
- Sorts unique elements for consecutive checking
- Tracks current sequence length and maximum found
- Handles edge cases properly
- Returns maximum consecutive sequence length

## Time & Space Complexity

**Time Complexity:** O(n log n)
- Converting to set: O(n)
- Sorting: O(n log n)
- Single pass through sorted array: O(n)
- Total: O(n log n)

**Space Complexity:** O(n)
- Set storage: O(n)
- Sorted array: O(n)
- Counter array: O(n)
- Total: O(n)

## Key Insights

1. **Duplicate Removal:** Using a set removes duplicates, which simplifies the consecutive sequence finding.

2. **Sorting Advantage:** After sorting, consecutive elements are adjacent, making it easy to count sequences.

3. **Sequence Tracking:** We can track the current sequence length and update the maximum when a sequence breaks.

4. **Edge Cases:** Arrays with less than 2 elements have simple solutions.

5. **Consecutive Check:** Two numbers are consecutive if their difference is exactly 1.

6. **Efficient Counting:** We can count consecutive sequences in a single pass through the sorted array.

## Mistakes Made

1. **Wrong Complexity:** Not achieving O(n) time complexity as required by the problem.

2. **Duplicate Handling:** Not properly handling duplicate elements.

3. **Complex Logic:** Overcomplicating the consecutive sequence detection.

4. **Edge Cases:** Not handling empty arrays or single elements properly.

## Related Problems

- **Longest Increasing Subsequence** (Problem 300): Find longest increasing subsequence
- **Longest Common Subsequence** (Problem 1143): Find longest common subsequence
- **Longest Palindromic Substring** (Problem 5): Find longest palindromic substring
- **Longest Substring Without Repeating Characters** (Problem 3): Find longest unique substring

## Alternative Approaches

1. **Hash Set with O(n):** Use hash set to check consecutive elements without sorting - O(n) time
2. **Union Find:** Use union-find data structure to group consecutive elements - O(n) time
3. **Two Pass:** First pass to build hash set, second pass to find sequences - O(n) time

## Common Pitfalls

1. **Wrong Complexity:** Using sorting when O(n) solution is required.
2. **Duplicate Issues:** Not properly handling duplicate elements.
3. **Complex Implementation:** Overcomplicating the consecutive sequence detection.
4. **Edge Cases:** Not handling empty arrays or single elements.
5. **Inefficient Approach:** Not using hash set for O(1) lookups.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/128.longest-consecutive-sequence.py)](../exercises/128.longest-consecutive-sequence.py)

*Note: This is a hash table problem that demonstrates finding consecutive sequences, though this solution doesn't achieve the required O(n) time complexity.*
