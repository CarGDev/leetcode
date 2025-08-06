# Majority Element

[![Problem 169](https://img.shields.io/badge/Problem-169-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/majority-element/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/majority-element/)

**Problem Number:** [169](https://leetcode.com/problems/majority-element/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** Array, Hash Table, Divide and Conquer, Sorting, Counting
**LeetCode Link:** [https://leetcode.com/problems/majority-element/](https://leetcode.com/problems/majority-element/)

## Problem Description

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**
```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## My Approach

I used a **Sorting** approach to find the majority element. The key insight is that after sorting, the majority element will always be at the middle position since it appears more than half the time.

**Algorithm:**
1. Sort the array in ascending order
2. Return the element at the middle index (n/2)
3. The majority element is guaranteed to be at this position

## Solution

The solution uses sorting to find the majority element efficiently. See the implementation in the [solution file](../exercises/169.majority-element.py).

**Key Points:**
- Sorts array to find middle element
- Majority element is guaranteed to be at n/2 position
- Simple and efficient approach
- Handles all edge cases automatically

## Time & Space Complexity

**Time Complexity:** O(n log n)
- Sorting: O(n log n)
- Accessing middle element: O(1)
- Total: O(n log n)

**Space Complexity:** O(1)
- In-place sorting (if using built-in sort)
- No additional data structures needed

## Key Insights

1. **Sorting Property:** After sorting, the majority element appears at the middle position.

2. **Majority Guarantee:** Since the majority element appears more than n/2 times, it must be at position n/2.

3. **Simple Solution:** This approach is straightforward and doesn't require complex logic.

4. **Guaranteed Existence:** The problem guarantees a majority element exists.

5. **Middle Position:** The majority element will always be at index len(nums)//2.

6. **No Counting Needed:** We don't need to count occurrences, just find the middle element.

## Mistakes Made

1. **Hash Table:** Initially might use hash table to count occurrences, requiring O(n) space.

2. **Linear Search:** Using linear search to find the most frequent element.

3. **Complex Logic:** Overcomplicating the solution with unnecessary counting.

4. **Wrong Position:** Not understanding that majority element is at middle position.

## Related Problems

- **Majority Element II** (Problem 229): Find elements appearing more than n/3 times
- **Single Number** (Problem 136): Find element appearing once
- **Single Number II** (Problem 137): Find element appearing once (others appear thrice)
- **Find the Duplicate Number** (Problem 287): Find duplicate in array

## Alternative Approaches

1. **Boyer-Moore Voting:** Use voting algorithm - O(n) time, O(1) space
2. **Hash Table:** Count occurrences - O(n) time, O(n) space
3. **Divide and Conquer:** Recursive approach - O(n log n) time, O(log n) space
4. **Randomization:** Random sampling - O(n) average time

## Common Pitfalls

1. **Hash Table Usage:** Using hash table when sorting is simpler.
2. **Complex Counting:** Manually counting occurrences instead of using sorting.
3. **Wrong Position:** Not understanding the middle position property.
4. **Space Inefficiency:** Using O(n) space when O(1) is possible.
5. **Over-engineering:** Using complex algorithms when simple sorting suffices.

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/169.majority-element.py)](../exercises/169.majority-element.py)

*Note: This is a simple sorting problem that demonstrates efficient majority element finding.*
