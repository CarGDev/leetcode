# Count Special Triplets

[![Problem 3583](https://img.shields.io/badge/Problem-3583-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/count-special-triplets/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/count-special-triplets/)

**Problem Number:** [3583](https://leetcode.com/problems/count-special-triplets/)
**Difficulty:** [Medium](https://leetcode.com/problemset/?difficulty=MEDIUM)
**Category:** Array, Hash Table, Two Pointers
**LeetCode Link:** [https://leetcode.com/problems/count-special-triplets/](https://leetcode.com/problems/count-special-triplets/)

## Problem Description

You are given a 0-indexed integer array `nums`. A triplet of indices `(i, j, k)` is a **special triplet** if the following conditions are met:

- `0 <= i < j < k < nums.length`
- `nums[i] * 2 == nums[j]`
- `nums[j] * 2 == nums[k]`

Return *the number of **special triplets***.

**Example 1:**
```
Input: nums = [1,2,4,8]
Output: 2
Explanation: The special triplets are:
- (0,1,2): nums[0] * 2 == nums[1] and nums[1] * 2 == nums[2]
- (1,2,3): nums[1] * 2 == nums[2] and nums[2] * 2 == nums[3]
```

**Example 2:**
```
Input: nums = [1,2,4,8,16]
Output: 4
Explanation: The special triplets are:
- (0,1,2): nums[0] * 2 == nums[1] and nums[1] * 2 == nums[2]
- (1,2,3): nums[1] * 2 == nums[2] and nums[2] * 2 == nums[3]
- (2,3,4): nums[2] * 2 == nums[3] and nums[3] * 2 == nums[4]
- (0,1,2,3): nums[0] * 2 == nums[1] and nums[1] * 2 == nums[2] and nums[2] * 2 == nums[3]
```

**Constraints:**
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## My Approach

I used a **Hash Table** approach with sliding window to count special triplets efficiently. The key insight is to track left and right counts for each middle element.

**Algorithm:**
1. Initialize hash tables for left and right counts
2. Pre-populate right count hash table
3. For each middle element (j):
   - Calculate target as nums[j] * 2
   - Get left count (elements before j that equal target)
   - Get right count (elements after j that equal target)
   - Add left_count * right_count to total
   - Update left count hash table
   - Decrement right count hash table

## Solution

The solution uses hash tables to efficiently count special triplets. See the implementation in the [solution file](../exercises/3583.count-special-triplets.py).

**Key Points:**
- Uses hash tables for O(1) lookup
- Tracks left and right counts
- Updates counts dynamically
- Handles large numbers with modulo

## Time & Space Complexity

**Time Complexity:** O(n)
- Single pass through array: O(n)
- Hash table operations: O(1) average
- Total: O(n)

**Space Complexity:** O(n)
- Hash tables for left and right counts: O(n)
- Total: O(n)

## Key Insights

1. **Hash Table Tracking:** Use hash tables to track element frequencies.

2. **Sliding Window:** Update counts as we move through the array.

3. **Triplet Counting:** For each middle element, count valid left and right pairs.

4. **Dynamic Updates:** Update left and right counts efficiently.

5. **Modulo Operation:** Handle large numbers with modulo arithmetic.

6. **Efficient Lookup:** O(1) lookup for element frequencies.

## Mistakes Made

1. **Wrong Counting:** Initially might count triplets incorrectly.

2. **Complex Logic:** Overcomplicating the triplet counting.

3. **Update Issues:** Not properly updating left and right counts.

4. **Inefficient Approach:** Using O(n³) approach when hash table suffices.

## Related Problems

- **3Sum** (Problem 15): Find triplets with target sum
- **Two Sum** (Problem 1): Find pair with target sum
- **Contains Duplicate** (Problem 217): Check for duplicates
- **Majority Element** (Problem 169): Find majority element

## Alternative Approaches

1. **Brute Force:** Check all triplets - O(n³) time
2. **Two Pointers:** Use two pointers for each middle element - O(n²) time
3. **Binary Search:** Use binary search for target elements - O(n log n) time

## Common Pitfalls

1. **Wrong Counting:** Not counting triplets correctly.
2. **Complex Logic:** Overcomplicating the triplet counting.
3. **Update Issues:** Not properly updating left and right counts.
4. **Inefficient Approach:** Using O(n³) approach when hash table suffices.
5. **Overflow:** Not handling large numbers properly.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/3583.count-special-triplets.py)](../exercises/3583.count-special-triplets.py)

*Note: This is a hash table problem that demonstrates efficient triplet counting with sliding window technique.*
